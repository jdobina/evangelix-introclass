import os
import unittest
import subprocess

class TestAll(unittest.TestCase):
    oracle_dir = os.path.dirname(os.path.realpath(__file__))
    oracle = os.path.join(oracle_dir, 'oracle_ext')

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

    def test_7(self):
        rc = self._run_oracle(7)
        self.assertEqual(rc, 0)

    def test_8(self):
        rc = self._run_oracle(8)
        self.assertEqual(rc, 0)

    def test_9(self):
        rc = self._run_oracle(9)
        self.assertEqual(rc, 0)

    def test_10(self):
        rc = self._run_oracle(10)
        self.assertEqual(rc, 0)

    def test_11(self):
        rc = self._run_oracle(11)
        self.assertEqual(rc, 0)

    def test_12(self):
        rc = self._run_oracle(12)
        self.assertEqual(rc, 0)

    def test_13(self):
        rc = self._run_oracle(13)
        self.assertEqual(rc, 0)

    def test_14(self):
        rc = self._run_oracle(14)
        self.assertEqual(rc, 0)

    def test_15(self):
        rc = self._run_oracle(15)
        self.assertEqual(rc, 0)

    def test_16(self):
        rc = self._run_oracle(16)
        self.assertEqual(rc, 0)

if __name__ == '__main__':
    unittest.main()
