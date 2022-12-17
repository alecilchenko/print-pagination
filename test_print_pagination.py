import unittest
from print_pagination import *
import io
from contextlib import redirect_stdout

class TestPagination(unittest.TestCase):

    def setUp(self):
        # Create a new StringIO object before each test
        self.buf = io.StringIO()

    def test_current_page_too_low(self):
        # Test current page less than 1
        with redirect_stdout(self.buf):
            print_pagination(0, 10, 2, 2)
        output = self.buf.getvalue().strip()

        # Compare the output to the expected result
        self.assertEqual(output, "Current page should be at least 1 or bigger")

    def test_current_page_too_high(self):
        # Test current page greater than total pages
        with redirect_stdout(self.buf):
            print_pagination(11, 10, 2, 2)
        output = self.buf.getvalue().strip()

        # Compare the output to the expected result
        self.assertEqual(output, "Current page cannot be bigget than total")

    def test_total_pages_too_low(self):
        # Test total pages less than 1
        with redirect_stdout(self.buf):
            print_pagination(1, 0, 2, 2)
        output = self.buf.getvalue().strip()

        # Compare the output to the expected result
        self.assertEqual(output, "Total page should be at least 1 or bigger")

    def test_boundaries_too_low(self):
        # Test boundaries less than 0
        with redirect_stdout(self.buf):
            print_pagination(1, 10, -1, 2)
        output = self.buf.getvalue().strip()

        # Compare the output to the expected result
        self.assertEqual(output, "Boundaries cannot be negative")

    def test_boundaries_too_high(self):
        # Test boundaries greater than half of total pages
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 6, 2)
        output = self.buf.getvalue().strip()

        # Compare the output to the expected result
        self.assertEqual(output, "Boundaries cannot be more than half of total")

    def test_around_too_low(self):
        # Test around less than 0
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 2, -1)
        output = self.buf.getvalue().strip()

        # Compare the output to the expected result
        self.assertEqual(output, "Around cannot be negative")
    
    def test_around_invalid(self):
        # Test around more than half of total
        with redirect_stdout(self.buf):
            print_pagination(1, 1, 0, 1)
        output = self.buf.getvalue().strip()

        # Compare the output to the expected result
        self.assertEqual(output, "Around cannot be more than half of total")

    def test_pagination(self):
        # Test pagination output with various parameters
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 2, 2)
            print_pagination(5, 10, 2, 2)
            print_pagination(8, 10, 2, 2)
            print_pagination(10, 10, 2, 2)
        output = self.buf.getvalue().strip()
        self.assertEqual(output, '1 2 3 ... 9 10\n1 2 3 4 5 6 7 ... 9 10\n1 2 ... 6 7 8 9 10\n1 2 ... 8 9 10')

    def test_more_pagination(self):
        # Test pagination output with another input
        with redirect_stdout(self.buf):
            print_pagination(1, 10, 5, 5)
            print_pagination(100, 101, 3, 1)
            print_pagination(39, 333, 3, 3)
            print_pagination(1, 2, 1, 0)
        output = self.buf.getvalue().strip()
        self.assertEqual(output, '1 2 3 4 5 6 7 8 9 10\n1 2 3 ... 99 100 101\n1 2 3 ... 36 37 38 39 40 41 42 ... 331 332 333\n1 2')

    def test_edge_case(self):
        # Test pagination with edge cases, when around and boundries == zero
        with redirect_stdout(self.buf):
            print_pagination(1, 1, 0, 0)
            print_pagination(10, 10, 0, 0)
        output = self.buf.getvalue().strip()
        self.assertEqual(output, '1\n10')


if __name__ == '__main__':
    unittest.main()