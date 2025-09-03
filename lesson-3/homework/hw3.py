# 1. Create and Access List Elements
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Third fruit:", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated list:", combined_list)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50, 60, 70]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("Extracted list:", new_list)

# 4. Convert List to Tuple
movies = ["Inception", "Titanic", "Avatar", "Interstellar", "Joker"]
movies_tuple = tuple(movies)
print("Movies as tuple:", movies_tuple)

# 5. Check Element in a List
cities = ["London", "Paris", "New York", "Tokyo"]
print("Is Paris in the list?", "Paris" in cities)

# 6. Duplicate a List Without Using Loops
nums = [1, 2, 3]
duplicate = nums * 2
print("Duplicated list:", duplicate)

# 7. Swap First and Last Elements of a List
swap_list = [10, 20, 30, 40, 50]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("Swapped list:", swap_list)

# 8. Slice a Tuple
numbers_tuple = (1,2,3,4,5,6,7,8,9,10)
print("Slice 3 to 7:", numbers_tuple[3:8])

# 9. Count Occurrences in a List
colors = ["blue", "red", "blue", "green", "blue", "yellow"]
print("Blue appears:", colors.count("blue"), "times")

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger")
print("Index of lion:", animals.index("lion"))

# 11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print("Merged tuple:", merged)

# 12. Find the Length of a List and Tuple
sample_list = [1, 2, 3, 4]
sample_tuple = (5, 6, 7)
print("Length of list:", len(sample_list))
print("Length of tuple:", len(sample_tuple))

# 13. Convert Tuple to List
tuple_numbers = (10, 20, 30, 40, 50)
list_numbers = list(tuple_numbers)
print("Converted list:", list_numbers)

# 14. Find Maximum and Minimum in a Tuple
num_tuple = (7, 2, 9, 4, 1)
print("Maximum:", max(num_tuple))
print("Minimum:", min(num_tuple))

# 15. Reverse a Tuple
words = ("python", "java", "c++", "ruby")
print("Reversed tuple:", words[::-1])
