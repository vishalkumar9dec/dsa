import unittest

from third import get_subset_equals


class TestGetSubsetEquals(unittest.TestCase):
    def test_example_true(self):
        self.assertTrue(get_subset_equals([3, 34, 4, 12, 5, 2], 9))

    def test_example_false(self):
        self.assertFalse(get_subset_equals([3, 34, 4, 12, 5, 2], 30))

    def test_single_element_match(self):
        self.assertTrue(get_subset_equals([5], 5))

    def test_single_element_no_match(self):
        self.assertFalse(get_subset_equals([5], 4))

    def test_target_larger_than_total(self):
        self.assertFalse(get_subset_equals([3, 34, 4, 12, 5, 2], 100))

    def test_whole_array_sums_to_target(self):
        self.assertTrue(get_subset_equals([1, 2, 3], 6))

    def test_input_order_does_not_matter(self):
        self.assertTrue(get_subset_equals([2, 5, 3, 4], 9))

    def test_sorts_input_in_place(self):
        arr = [3, 1, 2]
        get_subset_equals(arr, 3)
        self.assertEqual(arr, [1, 2, 3])

    # The cases below are correct subset-sum answers that the current
    # implementation gets wrong: it only ever checks prefix sums of the sorted
    # array (left advances but is never subtracted from running_sum), so a
    # subset that skips a smaller element is missed.
    @unittest.expectedFailure
    def test_non_prefix_subset(self):
        self.assertTrue(get_subset_equals([1, 2, 3], 5))  # 2 + 3

    @unittest.expectedFailure
    def test_non_contiguous_subset(self):
        self.assertTrue(get_subset_equals([3, 34, 4, 12, 5, 2], 37))  # 3 + 34

    @unittest.expectedFailure
    def test_empty_array_zero_target(self):
        self.assertTrue(get_subset_equals([], 0))  # empty subset sums to 0


if __name__ == "__main__":
    unittest.main()
