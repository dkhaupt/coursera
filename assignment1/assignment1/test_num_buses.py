import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_no_buses(self):
        """Testing that zero people should warrant zero buses"""

        expected = 0
        actual = a1.num_buses(0)

        self.assertEqual(expected, actual)

    def test_low_buses(self):

        expected = 1
        actual = a1.num_buses(25)

        self.assertEqual(expected, actual)

    def test_high_buses(self):

        expected = 11
        actual = a1.num_buses(501)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
