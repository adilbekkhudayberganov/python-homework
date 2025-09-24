# Sample dictionary
my_dict = {1: 2, 3: 1, 2: 4}

# Ascending
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc)

# Descending
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc)


my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)
# Output: {0: 10, 1: 20, 2: 30}


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

print(result)
# Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


squares_15 = {x: x*x for x in range(1, 16)}
print(squares_15)


my_set = {1, 2, 3}
print(my_set)


my_set = {1, 2, 3, 4}
for item in my_set:
    print(item)


my_set = {1, 2}
my_set.add(3)         # Add single
my_set.update([4, 5]) # Add multiple
print(my_set)


my_set = {1, 2, 3, 4}
my_set.remove(2)   # Removes 2 (error if not exists)
print(my_set)


my_set = {1, 2, 3}
my_set.discard(2)   # Removes 2 safely (no error if missing)
print(my_set)


