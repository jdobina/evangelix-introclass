import argparse
import json
import os
import subprocess
import time

PROGRAMS = ('checksum', 'digits', 'grade', 'median', 'smallest', 'syllables')

def get_defects(program):
    defects = []

    program_metadata_json = os.path.join(program, 'program-metadata.json')
    with open(program_metadata_json) as f:
        program_metadata = json.load(f)

    for unique_defect in sorted(program_metadata['uniqueDefects'],
                                key=lambda x: x['repo'] + x['revision']):
        metadata_json = os.path.join(program,
                                     unique_defect['repo'],
                                     unique_defect['revision'],
                                     'metadata.json')
        with open(metadata_json) as f:
            metadata = json.load(f)

        if len(metadata['blackbox']['fail']) > 0:
            defects.append((unique_defect['repo'], unique_defect['revision']))

    return defects

def run_exp(tool, programs, iterations, tool_args):
    run_defect_exp_dir = os.path.dirname(os.path.realpath(__file__))
    run_defect_exp = os.path.join(run_defect_exp_dir, 'run_defect_exp')

    for program in sorted(programs):
        defects = get_defects(program)
        num_defects = len(defects)
        i = 0
        for repo, revision in defects:
            i += 1
            print(('running defect experiment [{}/{}]'
                   '\nprogram: {}'
                   '\nrepo: {}'
                   '\nrevision: {}'
                  ).format(i, num_defects, program, repo, revision))
            start = time.time()
            retcode = subprocess.call([run_defect_exp,
                                       tool,
                                       program,
                                       repo,
                                       revision,
                                       str(iterations),
                                       tool_args],
                                      stdout=subprocess.DEVNULL,
                                      stderr=subprocess.DEVNULL)
            end = time.time()
            if retcode == 0:
                print(('defect experiment finished in {}s'
                      ).format(int(end - start)))
            else:
                print(('defect experiment failed with retcode: {}'
                      ).format(retcode))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='run repair experiment')
    parser.add_argument('tool', choices=('angelix', 'evangelix'),
                        help='tool to use for repair')
    parser.add_argument('programs', nargs='+',
                        choices=PROGRAMS,
                        default=PROGRAMS,
                        help='programs to repair')
    parser.add_argument('iterations', type=int,
                        help='number of repair iterations for each defect')
    parser.add_argument('tool_args', help='tool arguments')
    args = parser.parse_args()

    run_exp(args.tool, args.programs, args.iterations, args.tool_args)