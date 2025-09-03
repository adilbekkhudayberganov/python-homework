1. Leap Year Function
Question

Write a function is_leap(year) that determines if a given year is a leap year.

Rules:

Divisible by 4 → leap year

Except divisible by 100 → not leap year

But divisible by 400 → leap year

Solution
def is_leap(year):
    """
    Determines whether a given year is a leap year.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage:
year = 2024
print(f"{year} is a leap year:", is_leap(year))


Example Output

2024 is a leap year: True

2. Conditional Statements Exercise
Question

Given an integer n, print:

"Weird" if n is odd

"Not Weird" if n is even and in 2..5

"Weird" if n is even and in 6..20

"Not Weird" if n is even and >20

Solution
n = int(input("Enter a positive integer n: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


Sample Run

Input: 3
Output: Weird

3. Even Numbers Between Two Integers Without Loops
Question

Given two integers a and b (inclusive), print all even numbers between them. Provide two solutions:

Solution 1: using if-else

Solution 2: without if-else

Solution 1 (with if-else)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Ensure a <= b
if a > b:
    a, b = b, a

# Start from the first even number
if a % 2 != 0:
    a += 1

even_numbers = list(range(a, b + 1, 2))
print("Even numbers:", even_numbers)
