import argparse
import csv
import json
import os
import re
import sys

PROGRAMS = ('checksum', 'digits', 'grade', 'median', 'smallest', 'syllables')
TOOLS = ('angelix', 'evangelix')
REPAIRS = ('repair_bb', 'repair_all')
FIELDNAMES = (
    'program',
    'repo',
    'revision',
    'nondeterministic',
    'blackbox_pass_count',
    'blackbox_fail_count',
    'whitebox_pass_count',
    'whitebox_fail_count',
    'instr_blackbox_pass_count',
    'instr_blackbox_fail_count',
    'instr_whitebox_pass_count',
    'instr_whitebox_fail_count',
    'angelix_experiment',
    'angelix_repair_bb',
    'angelix_repair_bb_partial',
    'angelix_repair_bb_transforms',
    'angelix_repair_bb_time',
    'angelix_repair_bb_blackbox_pass_count',
    'angelix_repair_bb_blackbox_fail_count',
    'angelix_repair_bb_whitebox_pass_count',
    'angelix_repair_bb_whitebox_fail_count',
    'angelix_repair_all',
    'angelix_repair_all_partial',
    'angelix_repair_all_transforms',
    'angelix_repair_all_time',
    'angelix_repair_all_blackbox_pass_count',
    'angelix_repair_all_blackbox_fail_count',
    'angelix_repair_all_whitebox_pass_count',
    'angelix_repair_all_whitebox_fail_count',
    'evangelix_experiment',
    'evangelix_repair_bb',
    'evangelix_repair_bb_partial',
    'evangelix_repair_bb_transforms',
    'evangelix_repair_bb_time',
    'evangelix_repair_bb_blackbox_pass_count',
    'evangelix_repair_bb_blackbox_fail_count',
    'evangelix_repair_bb_whitebox_pass_count',
    'evangelix_repair_bb_whitebox_fail_count',
    'evangelix_repair_all',
    'evangelix_repair_all_partial',
    'evangelix_repair_all_transforms',
    'evangelix_repair_all_time',
    'evangelix_repair_all_blackbox_pass_count',
    'evangelix_repair_all_blackbox_fail_count',
    'evangelix_repair_all_whitebox_pass_count',
    'evangelix_repair_all_whitebox_fail_count',
)

def parse_angelix_log(angelix_log):
    info = dict.fromkeys(
            ['repaired',
             'repair_partial',
             'repair_time',
             'repair_transforms'])

    patch_gen_regex = re.compile(r'''^INFO\s+repair\s+
                                     (?P<patch>partial\s+patch|patch)\s+
                                     successfully\s+generated\s+in\s+
                                     (?P<repair_time>\d+)s
                                     .*$
                                  ''', re.X)
    no_patch_regex = re.compile(r'^.*no patch generated in (?P<repair_time>\d+)s$')
    apply_transform_regex = re.compile(r'^.*applied (?P<transform>.+) transform$')
    revert_transform_regex = re.compile(r'^.*reverting (?P<transform>.+) transform$')
    patch_sources_regex = re.compile(r'^.*patching sources$')
    partial_fix_regex = re.compile(r'^.*Saving partial fix$')

    info['repair_transforms'] = []
    for line in angelix_log:
        m = patch_gen_regex.match(line)
        if m:
            if m.group('patch') == 'patch':
                info['repaired'] = True
                info['repair_partial'] = False
            elif m.group('patch') == 'partial patch':
                info['repaired'] = False
                info['repair_partial'] = True
            info['repair_time'] = int(m.group('repair_time'))
            break

        m = no_patch_regex.match(line)
        if m:
            info['repaired'] = False
            info['repair_partial'] = False
            info['repair_time'] = int(m.group('repair_time'))
            break

        m = partial_fix_regex.match(line)
        if m:
            info['repair_transforms'].append('partial fix')
            continue

        m = patch_sources_regex.match(line)
        if m:
            info['repair_transforms'].append('patch sources')
            continue

        m = apply_transform_regex.match(line)
        if m:
            info['repair_transforms'].append('+' + m.group('transform'))
            continue

        m = revert_transform_regex.match(line)
        if m:
            info['repair_transforms'].append('-' + m.group('transform'))
            continue

    return info

def get_defect_results(config):
    results = []

    for program in sorted(config['programs']):
        program_metadata_json = os.path.join(program, 'program-metadata.json')
        with open(program_metadata_json) as f:
            program_metadata = json.load(f)

        for defect in sorted(program_metadata['uniqueDefects'],
                             key=lambda x: x['repo'] + x['revision']):
            defect_dir = os.path.join(program,
                                      defect['repo'],
                                      defect['revision'])

            metadata_json = os.path.join(defect_dir, 'metadata.json')
            with open(metadata_json) as f:
                metadata = json.load(f)

            if len(metadata['blackbox']['fail']) == 0:
                continue

            result = dict.fromkeys(FIELDNAMES)

            result['program'] = program
            result['repo'] = defect['repo']
            result['revision'] = defect['revision']
            result['nondeterministic'] = metadata['nondeterministic']
            result['blackbox_pass_count'] = len(metadata['blackbox']['pass'])
            result['blackbox_fail_count'] = len(metadata['blackbox']['fail'])
            result['whitebox_pass_count'] = len(metadata['whitebox']['pass'])
            result['whitebox_fail_count'] = len(metadata['whitebox']['fail'])

            instr_test_result_json = os.path.join(defect_dir, 'test_result.json')
            if not os.path.exists(instr_test_result_json):
                continue

            with open(instr_test_result_json) as f:
                instr_test_result = json.load(f)

            result['instr_blackbox_pass_count'] = len(instr_test_result['blackbox']['pass'])
            result['instr_blackbox_fail_count'] = len(instr_test_result['blackbox']['fail'])
            result['instr_whitebox_pass_count'] = len(instr_test_result['whitebox']['pass'])
            result['instr_whitebox_fail_count'] = len(instr_test_result['whitebox']['fail'])

            for tool in TOOLS:
                exp_ok_path = os.path.join(defect_dir, tool + '_exp_ok')
                exp_fail_path = os.path.join(defect_dir, tool + '_exp_fail')
                if os.path.exists(exp_ok_path):
                    result[tool + '_experiment'] = 'ok'
                elif os.path.exists(exp_fail_path):
                    result[tool + '_experiment'] = 'fail'
                    continue
                else:
                    result[tool + '_experiment'] = 'none'
                    continue

                for repair in REPAIRS:
                    repair_dir = os.path.join(defect_dir, 'results', tool,
                                              repair, '1')

                    angelix_log = os.path.join(repair_dir, '.angelix', 'angelix.log')
                    with open(angelix_log) as f:
                        info = parse_angelix_log(f)

                    result[tool + '_' + repair] = info['repaired']
                    result[tool + '_' + repair + '_partial'] = info['repair_partial']
                    result[tool + '_' + repair + '_transforms'] = "->".join(info['repair_transforms'])
                    result[tool + '_' + repair + '_time'] = info['repair_time']

                    repair_test_result_json = os.path.join(repair_dir, 'test_result.json')
                    if not os.path.exists(repair_test_result_json):
                        continue

                    with open(repair_test_result_json) as f:
                        repair_test_result = json.load(f)

                    result[tool + '_' + repair + '_blackbox_pass_count'] = (
                            len(repair_test_result['blackbox']['pass']))
                    result[tool + '_' + repair + '_blackbox_fail_count'] = (
                            len(repair_test_result['blackbox']['fail']))
                    result[tool + '_' + repair + '_whitebox_pass_count'] = (
                            len(repair_test_result['whitebox']['pass']))
                    result[tool + '_' + repair + '_whitebox_fail_count'] = (
                            len(repair_test_result['whitebox']['fail']))

            results.append(result)

    return results

def dump_csv(defect_results):
    csv_writer = csv.DictWriter(sys.stdout, fieldnames=FIELDNAMES)
    csv_writer.writeheader()
    csv_writer.writerows(defect_results)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate experiment report')
    parser.add_argument('-p', '--programs', nargs='+',
                        choices=PROGRAMS,
                        default=PROGRAMS,
                        help='programs to generate report')
    args = parser.parse_args()

    config = {}
    config['programs'] = args.programs

    defect_results = get_defect_results(config)
    dump_csv(defect_results)
