import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(s: str) -> int:
    """
    Counts the number of vowels in the input string (both lowercase and uppercase vowels).
    Parameters:
        s (str): The input string.
    Returns:
        int: The number of vowels found in the input string.
    """
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

# Part 2
def short_lists(lst: list[list[int]]) -> list[list[int]]:
    """
    Returns a new list consisting of sublists from the input list that have exactly 2 elements.
    Parameters:
        lst (list[list[int]]): A list of lists where each sublist contains integers.
    Returns:
        list[list[int]]: A list containing only those sublists that have a length of 2.
    """
    return [sublist for sublist in lst if len(sublist) == 2]

# Part 3
def ascending_pairs(lst: list[list[int]]) -> list[list[int]]:
    """
    Returns a new list where any sublist of length 2 in the input list has its elements sorted in ascending order.
    Parameters:
        lst (list[list[int]]): A list of lists where each sublist contains integers.
    Returns:
        list[list[int]]: A new list with sublists of length 2 sorted in ascending order.
    """
    result = []
    for sublist in lst:
        if len(sublist) == 2:
            result.append(sorted(sublist))
        else:
            result.append(sublist)
    return result

# Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents
def add_prices(price1: Price, price2: Price) -> Price:
    """
    Returns a new Price object that is the sum of the two input Price objects,
    with the number of cents normalized (i.e., not exceeding 99).
    Parameters:
        price1 (Price): The first price object to sum.
        price2 (Price): The second price object to sum.
    Returns:
        Price: A new Price object representing the sum.
    """
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    if total_cents >= 100:
        total_dollars += total_cents // 100
        total_cents = total_cents % 100

    return Price(total_dollars, total_cents)

# Part 5
class Rectangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def rectangle_area(rect: Rectangle) -> int:
    """
    Returns the area of a rectangle given its top-left and bottom-right coordinates.
    Parameters:
        rect (Rectangle): The rectangle object representing the axis-aligned rectangle.
    Returns:
        int: The area of the rectangle.
    """
    width = abs(rect.x2 - rect.x1)
    height = abs(rect.y1 - rect.y2)

    return width * height

# Part 6
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'Book(title="{self.title}", author="{self.author}")'

def books_by_author(author_name: str, books_list: list[Book]) -> list[Book]:
    """
    Returns a list of books written by the given author from a list of Book objects.
    Parameters:
        author_name (str): The name of the author.
        books_list (list[Book]): A list of Book objects.
    Returns:
        list[Book]: A list of books written by the specified author.
    """

    return [book for book in books_list if book.author == author_name]

# Part 7
import math
class Rectangle:
    def __init__(self, top_left: tuple[int, int], bottom_right: tuple[int, int]):
        self.top_left = top_left
        self.bottom_right = bottom_right
class Circle:
    def __init__(self, center: tuple[int, int], radius: float):
        self.center = center
        self.radius = radius
    def __repr__(self):
        return f'Circle(center={self.center}, radius={self.radius})'
def circle_bound(rect: Rectangle) -> Circle:
    """
    Returns the smallest bounding Circle for the given Rectangle. The circle is centered
    at the center of the rectangle and its radius is the distance from the center to one of its corners.
    Parameters:
        rect (Rectangle): The rectangle to enclose in a circle.
    Returns:
        Circle: The smallest circle that bounds the rectangle.
    """
    center_x = (rect.top_left[0] + rect.bottom_right[0]) / 2
    center_y = (rect.top_left[1] + rect.bottom_right[1]) / 2
    center = (center_x, center_y)
    corner_x, corner_y = rect.top_left
    radius = math.sqrt((center_x - corner_x) ** 2 + (center_y - corner_y) ** 2)

    return Circle(center, radius)

# Part 8
class Employee:
    def __init__(self, name: str, pay_rate: float):
        self.name = name
        self.pay_rate = pay_rate
def below_pay_average(employees: list[Employee]) -> list[str]:
    """
    Returns a list of names of employees whose pay is below the average pay of all employees in the input list.
    Parameters:
        employees (list[Employee]): A list of Employee objects.
    Returns:
        list[str]: A list of employee names whose pay is below the average pay.
    """

    if not employees:
        return []

    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)

    below_average = [employee.name for employee in employees if employee.pay_rate < average_pay]

    return below_average


