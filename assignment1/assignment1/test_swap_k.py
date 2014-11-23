import a1
import unittest

class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_no_swap(self):

        nums = [1, 2, 3, 4, 5, 6]
        nums_expected = [1, 2, 3, 4, 5, 6]
        k = 0
        a1.swap_k(nums,0)

        self.assertEqual(nums, nums_expected)

    def test_max_swap_even(self):

        nums = [1, 2, 3, 4, 5, 6]
        nums_expected = [4, 5, 6, 1, 2, 3]
        k = 3
        a1.swap_k(nums,k)

        self.assertEqual(nums, nums_expected)

    def test_max_swap_odd(self):

        nums = [1, 2, 3, 4, 5, 6, 7]
        nums_expected = [5, 6, 7, 4, 1, 2, 3]
        k = 3
        a1.swap_k(nums,k)

        self.assertEqual(nums, nums_expected)

if __name__ == '__main__':
    unittest.main(exit=False)
