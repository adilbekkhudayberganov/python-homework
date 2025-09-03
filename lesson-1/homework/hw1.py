# 1) Given a side of square. Find its perimeter and area.
s = float(input("Enter the side of the square: "))
perimeter_square = 4 * s
area_square = s ** 2
print(f"Square -> Perimeter: {perimeter_square}, Area: {area_square}")

# 2) Given diameter of circle. Find its length.
d = float(input("Enter the diameter of the circle: "))
circumference = math.pi * d
print(f"Circle -> Length (Circumference): {circumference}")

# 3) Given two numbers a and b. Find their mean.
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
mean_ab = (a + b) / 2
print(f"Mean of a and b: {mean_ab}")

# 4) Given two numbers a and b. Find their sum, product and square of each number.
sum_ab = a + b
prod_ab = a * b
a_sq = a ** 2
b_sq = b ** 2
print(f"Sum: {sum_ab}, Product: {prod_ab}, a^2: {a_sq}, b^2: {b_sq}")
