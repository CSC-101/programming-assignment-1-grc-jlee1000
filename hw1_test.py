import unittest
import math
from data import Price, Rectangle, Circle, Book, Employee
from hw1 import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_area, books_by_author, circle_bound, \
    below_pay_average

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        # Test 1: Input with only vowels
        self.assertEqual(vowel_count("AEIOUaeiou"), 10)
        # Test 2: Input with a mix of letters, numbers, and symbols
        self.assertEqual(vowel_count("Computer Science Class 123!"), 7)

    # Part 2
    def test_short_lists(self):
        # Test 1: Input with varying lengths
        self.assertEqual(short_lists([[1, 2], [3, 4, 5], [6], [7, 8]]), [[1, 2], [7, 8]])
        # Test 2: Input with only sublists of length 2
        self.assertEqual(short_lists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
        # Test 3: Input with mixed integer lists
        self.assertEqual(short_lists([[10], [20, 30], [40, 50, 60], [70, 80]]), [[20, 30], [70, 80]])

    # Part 3
    def test_ascending_pairs(self):
        # Test 1: Mixed input with sublists of length 2 and other lengths
        self.assertEqual(ascending_pairs([[2, 1], [4, 5, 6], [3, 2]]), [[1, 2], [4, 5, 6], [2, 3]])
        # Test 2: Input with sublists of length 1, 2, and 3
        self.assertEqual(ascending_pairs([[8, 4], [7], [9, 3, 2]]), [[4, 8], [7], [9, 3, 2]])

    # Part 4
    def test_add_prices(self):
        # Test 1: Addition with overflow in cents
        p1 = Price(5, 50)
        p2 = Price(3, 75)
        result = add_prices(p1, p2)
        self.assertEqual((result.dollars, result.cents), (9, 25))
        # Test 2: Addition with 99 and 1 cent (overflow by 1 cent)
        p1 = Price(1, 99)
        p2 = Price(0, 2)
        result = add_prices(p1, p2)
        self.assertEqual((result.dollars, result.cents), (2, 1))

    # Part 5
    def test_rectangle_area(self):
        # Test 1: Simple rectangle with positive dimensions
        rect1 = Rectangle(1, 3, 4, 1)
        self.assertEqual(rectangle_area(rect1), 6)
        # Test 2: Larger rectangle
        rect2 = Rectangle(2, 5, 5, 2)
        self.assertEqual(rectangle_area(rect2), 9)

    # Part 6
    def test_books_by_author(self):
        # Book instances
        book1 = Book("Moby-Dick", "Herman Melville")
        book2 = Book("Beach Read", "Emily Henry")
        book3 = Book("The Lion, The Witch, and The Wardrobe", "C.S. Lewis")
        books = [book1, book2, book3]

        # Test 1: Books by Emily Henry
        result = books_by_author("Emily Henry", books)
        self.assertEqual(result, [book2])
        # Test 2: No books by an unknown author
        result = books_by_author("Rick Riordan", books)
        self.assertEqual(result, [])

    # Part 7
    def test_circle_bound(self):
        # Test 1: Rectangle with simple integer coordinates
        rect1 = Rectangle((1, 3), (5, 1))
        circle1 = circle_bound(rect1)
        self.assertEqual(circle1.center, (3.0, 2.0))
        self.assertAlmostEqual(circle1.radius, math.sqrt(4 + 1), places=9)

        # Test 2: Larger rectangle
        rect2 = Rectangle((0, 0), (6, 8))
        circle2 = circle_bound(rect2)
        self.assertEqual(circle2.center, (3.0, 4.0))
        self.assertAlmostEqual(circle2.radius, 5.0, places=9)

    # Part 8
    def test_below_pay_average(self):
        # Test 1: Basic case
        emp1 = Employee("Alice", 50000)
        emp2 = Employee("Bob", 60000)
        emp3 = Employee("Charlie", 40000)
        self.assertEqual(below_pay_average([emp1, emp2, emp3]), ["Charlie"])

        # Test 3: One employee exactly at the average
        emp6 = Employee("Frank", 55000)
        self.assertEqual(below_pay_average([emp1, emp2, emp6]), ["Alice"])


if __name__ == '__main__':
    unittest.main()
