import argparse
import csv
import json
import os
import sys

def get_unique_defects():
    programs = ('checksum', 'digits', 'grade', 'median', 'smallest', 'syllables')

    unique_defects = []
    for program in programs:
        program_metadata_json = os.path.join(program, 'program-metadata.json')
        with open(program_metadata_json) as f:
            program_metadata = json.load(f)

        for unique_defect in sorted(program_metadata['uniqueDefects'],
                                    key=lambda x: x['repo']):
            metadata_json = os.path.join(program,
                                         unique_defect['repo'],
                                         unique_defect['revision'],
                                         'metadata.json')
            with open(metadata_json) as f:
                metadata = json.load(f)

            unique_defects.append({
                'program': program,
                'repo': unique_defect['repo'],
                'revision': unique_defect['revision'],
                'nondeterministic': 'true' if metadata['nondeterministic'] else 'false',
                'blackbox_pass_count': len(metadata['blackbox']['pass']),
                'blackbox_fail_count': len(metadata['blackbox']['fail']),
                'whitebox_pass_count': len(metadata['whitebox']['pass']),
                'whitebox_fail_count': len(metadata['whitebox']['fail'])
            })

    return unique_defects

def dump_csv(unique_defects):
    fieldnames = (
        'program',
        'repo',
        'revision',
        'nondeterministic',
        'blackbox_pass_count',
        'blackbox_fail_count',
        'whitebox_pass_count',
        'whitebox_fail_count'
    )

    csv_writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(unique_defects)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='dump a CSV of unique defects')
    args = parser.parse_args()
    unique_defects = get_unique_defects()
    dump_csv(unique_defects)
