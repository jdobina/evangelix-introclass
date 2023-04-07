import argparse
import json
import sys
import unittest

def run_box_tests(runner, suite):
    result = runner.run(suite)
    all_tests = set([str(i) for i in range(1, result.testsRun + 1)])
    failed_tests = set([x[0].id().split('.')[2].split('_')[1]
                        for x in result.failures])
    passed_tests = all_tests - failed_tests

    return {
        'pass': list(passed_tests),
        'fail': list(failed_tests)
    }

def run_tests(test_dir):
    sys.path.append(test_dir)
    import test_bb
    import test_wb
    import test_all

    result = {}
    runner = unittest.TextTestRunner()

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_bb.TestBlackBox)
    result['blackbox'] = run_box_tests(runner, suite)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_wb.TestWhiteBox)
    result['whitebox'] = run_box_tests(runner, suite)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_all.TestAll)
    result['all'] = run_box_tests(runner, suite)

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='run blackbox and whitebox tests')
    parser.add_argument('test_dir', help='test directory')
    args = parser.parse_args()

    result = run_tests(args.test_dir)
    json.dump(result, sys.stdout)
