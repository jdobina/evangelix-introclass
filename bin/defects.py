import argparse
import csv
import json
import os
import sys

def get_defects():
    programs = ('checksum', 'digits', 'grade', 'median', 'smallest', 'syllables')

    defects = []
    for program in programs:
        for repo in sorted(os.listdir(program)):
            if len(repo) != 128:
                continue

            repo_dir = os.path.join(program, repo)

            for revision in sorted(os.listdir(repo_dir)):
                if len(revision) != 3:
                    continue

                metadata_json = os.path.join(repo_dir,
                                             revision,
                                             'metadata.json')
                with open(metadata_json) as f:
                    metadata = json.load(f)

                defects.append({
                    'program': program,
                    'repo': repo,
                    'revision': revision,
                    'nondeterministic': 'true' if metadata['nondeterministic'] else 'false',
                    'blackbox_pass_count': len(metadata['blackbox']['pass']),
                    'blackbox_fail_count': len(metadata['blackbox']['fail']),
                    'whitebox_pass_count': len(metadata['whitebox']['pass']),
                    'whitebox_fail_count': len(metadata['whitebox']['fail'])
                })

    return defects

def dump_csv(defects):
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
    csv_writer.writerows(defects)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='dump a CSV of defects')
    args = parser.parse_args()
    defects = get_defects()
    dump_csv(defects)
