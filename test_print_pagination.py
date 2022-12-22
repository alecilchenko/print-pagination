import unittest
from print_pagination import *
import io
from contextlib import redirect_stdout

class TestPagination(unittest.TestCase):

    def setUp(self):
        # Create a new StringIO object before each test
        self.buf = io.StringIO()

    def test_current_page_less_than_1(self):
        with self.assertRaises(ValueError):
            print_pagination(0, 10, 2, 2)

    def test_total_pages_less_than_1(self):
        with self.assertRaises(ValueError):
            print_pagination(1, 0, 2, 2)

    def test_current_page_greater_than_total_pages(self):
        with self.assertRaises(ValueError):
            print_pagination(11, 10, 2, 2)

    def test_boundaries_less_than_0(self):
        with self.assertRaises(ValueError):
            print_pagination(1, 10, -1, 2)

    def test_around_less_than_0(self):
        with self.assertRaises(ValueError):
            print_pagination(1, 10, 2, -1)

    def test_around_and_boundaries_0(self):
        with redirect_stdout(self.buf):
            print_pagination(10, 10, 0, 0)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '10')  

    def test_around_more_than_half_of_total_pages(self):
        with redirect_stdout(self.buf):
            print_pagination(10, 10, 0, 6)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 3 4 5 6 7 8 9 10')

    def test_boundaries_more_than_half_of_total_pages(self):
        with redirect_stdout(self.buf):
            print_pagination(10, 10, 6, 0)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 3 4 5 6 7 8 9 10')

    def test_normal_case(self):
        with redirect_stdout(self.buf):
            print_pagination(5, 10, 5, 2)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 3 4 5 6 7 8 9 10')

    def test_current_page_near_start_boundaries(self):
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 3, 1)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 3 ... 8 9 10')

    def test_current_page_near_end_boundaries(self):
        with redirect_stdout(self.buf):
            print_pagination(8, 10, 2, 2)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 ... 6 7 8 9 10')

    def test_current_page_in_middle(self):
        with redirect_stdout(self.buf):
            print_pagination(5, 10, 2, 1)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 ... 4 5 6 ... 9 10')

    def test_current_last_boundries_zero(self):
        # Test case when [... nums]
        with redirect_stdout(self.buf):
            print_pagination(10, 10, 0, 1)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '... 9 10')

    def test_current_near_end_boundries_zero(self):
        with redirect_stdout(self.buf):
            print_pagination(9, 10, 0, 1)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '... 8 9 10')

    def test_current_first_boundries_zero(self):
        # Test case when [nums ...]
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 0, 1)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 ...')

    def test_current_middle_boundries_zero(self):
        # Test case when [... nums ...]
        with redirect_stdout(self.buf):
            print_pagination(5, 10, 0, 1)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '... 4 5 6 ...')

    def test_current_first_around_zero(self):
        # Test case when [nums ... nums]
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 1, 0)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 ... 10')

    def test_current_last_around_zero(self):
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 1, 0)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 ... 10')

    def test_current_middle_around_zero(self):
        # Test case when [nums ... num ... nums]
        with redirect_stdout(self.buf):
            print_pagination(5, 10, 2, 0)
        output = self.buf.getvalue().strip()

        self.assertEqual(output, '1 2 ... 5 ... 9 10')

if __name__ == '__main__':
    unittest.main()