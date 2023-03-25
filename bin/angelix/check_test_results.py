import json
import os
import sys
import unittest

sys.path.append('../../../angelix-bin')
import test_bb
import test_wb
import test_all

def check_failures(unittest_failures, metadata_failures):
    assert(len(unittest_failures) == len(metadata_failures))
    for failure in unittest_failures:
        test = failure[0].id().split('.')[2].split('_')[1]
        assert(test in metadata_failures)

def check_bb(runner, metadata):
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_bb.TestBlackBox)
    result = runner.run(suite)
    check_failures(result.failures, metadata['blackbox']['fail'])

def check_wb(runner, metadata):
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_wb.TestWhiteBox)
    result = runner.run(suite)
    check_failures(result.failures, metadata['whitebox']['fail'])

def check_all(runner, metadata):
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_all.TestAll)
    result = runner.run(suite)
    bb_tests = metadata['blackbox']['pass'] + metadata['blackbox']['fail']
    wb_failures = [str(int(x) + len(bb_tests)) for x in metadata['whitebox']['fail']]
    check_failures(result.failures,
                   metadata['blackbox']['fail'] + wb_failures)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    with open('../metadata.json') as f:
        metadata = json.load(f)
    check_bb(runner, metadata)
    check_wb(runner, metadata)
    check_all(runner, metadata)
