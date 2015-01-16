import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_empty_changes(self):

        expected = (0, 0)
        actual = a1.stock_price_summary([])

        self.assertEqual(expected, actual)
    
    def test_no_pos(self):

        expected = (0, -.5)
        actual = a1.stock_price_summary([0,-0.1,-0.4])

        self.assertEqual(expected, actual)

    def test_no_neg(self):

        expected = (.5, 0)
        actual = a1.stock_price_summary([0,0.1,0.4])

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
