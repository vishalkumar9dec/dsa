import contextlib
import io
import sys
import unittest

from second import verify_ref_call


def run_and_capture():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        verify_ref_call()
    return buf.getvalue().splitlines()


class TestVerifyRefCall(unittest.TestCase):
    def test_prints_four_lines(self):
        self.assertEqual(len(run_and_capture()), 4)

    def test_refcount_drops_by_one_after_del(self):
        lines = run_and_capture()
        before, after = int(lines[0]), int(lines[1])
        self.assertEqual(before - after, 1)

    def test_refcount_counts_all_aliases(self):
        # absolute value varies by Python version (getrefcount's own argument
        # reference may or may not be counted), so only check a sane lower bound
        lines = run_and_capture()
        self.assertGreaterEqual(int(lines[0]), 3)
        self.assertGreaterEqual(int(lines[1]), 2)

    def test_append_through_alias_visible_via_other_names(self):
        lines = run_and_capture()
        self.assertEqual(lines[2], "[1, 2, 3, 4]")
        self.assertEqual(lines[3], "[1, 2, 3, 4]")

    def test_returns_none(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertIsNone(verify_ref_call())


class TestRefcountSemantics(unittest.TestCase):
    def test_aliases_share_identity(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)

    def test_del_alias_keeps_object_alive(self):
        a = [1, 2, 3]
        b = a
        del a
        self.assertEqual(b, [1, 2, 3])

    def test_getrefcount_increases_with_alias(self):
        a = [1, 2, 3]
        base = sys.getrefcount(a)
        b = a
        self.assertEqual(sys.getrefcount(a), base + 1)
        del b
        self.assertEqual(sys.getrefcount(a), base)


if __name__ == "__main__":
    unittest.main()
