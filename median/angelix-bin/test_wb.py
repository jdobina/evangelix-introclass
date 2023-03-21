import os
import unittest
import subprocess

class TestWhiteBox(unittest.TestCase):
    oracle_dir = os.path.dirname(os.path.realpath(__file__))
    oracle = os.path.join(oracle_dir, 'oracle_wb')

    def _run_oracle(self, test):
        return subprocess.call([self.oracle, str(test)], timeout=5)

    def test_1(self):
        rc = self._run_oracle(1)
        self.assertEqual(rc, 0)

    def test_2(self):
        rc = self._run_oracle(2)
        self.assertEqual(rc, 0)

    def test_3(self):
        rc = self._run_oracle(3)
        self.assertEqual(rc, 0)

    def test_4(self):
        rc = self._run_oracle(4)
        self.assertEqual(rc, 0)

    def test_5(self):
        rc = self._run_oracle(5)
        self.assertEqual(rc, 0)

    def test_6(self):
        rc = self._run_oracle(6)
        self.assertEqual(rc, 0)

if __name__ == '__main__':
    unittest.main()
