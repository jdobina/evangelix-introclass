import argparse
import json

def check_test_result(test_result, metadata):
    assert (set(test_result['blackbox']['pass'])
            == set(metadata['blackbox']['pass']))
    assert (set(test_result['blackbox']['fail'])
            == set(metadata['blackbox']['fail']))

    assert (set(test_result['whitebox']['pass'])
            == set(metadata['whitebox']['pass']))
    assert (set(test_result['whitebox']['fail'])
            == set(metadata['whitebox']['fail']))

    bb_tests = metadata['blackbox']['pass'] + metadata['blackbox']['fail']
    wb_passes = [str(int(x) + len(bb_tests))
                 for x in metadata['whitebox']['pass']]
    wb_failures = [str(int(x) + len(bb_tests))
                   for x in metadata['whitebox']['fail']]
    assert (set(test_result['all']['pass'])
            == set(metadata['blackbox']['pass'] + wb_passes))
    assert (set(test_result['all']['fail'])
            == set(metadata['blackbox']['fail'] + wb_failures))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='check test result')
    parser.add_argument('test_result_json', help='path to test result json')
    parser.add_argument('metadata_json', help='path to metadata json')
    args = parser.parse_args()
    with open(args.test_result_json) as tr, open(args.metadata_json) as m:
        test_result = json.load(tr)
        metadata = json.load(m)
        check_test_result(test_result, metadata)
