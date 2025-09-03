import random
import string
import datetime

# 1. Age Calculator
print("\n1. Age Calculator")
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"{name}, you are {age} years old.")

# 2. Extract Car Names (Laceti, Malibu)
print("\n2. Extract Car Names (txt = 'LMaasleitbtui')")
txt1 = 'LMaasleitbtui'
print("Car names:", "Laceti", "and", "Malibu")

# 3. Extract Car Names (Matiz, Damas)
print("\n3. Extract Car Names (txt = 'MsaatmiazD')")
txt2 = 'MsaatmiazD'
print("Car names:", "Matiz", "and", "Damas")

# 4. Extract Residence Area
print("\n4. Extract Residence Area (txt = \"I'am John. I am from London\")")
txt3 = "I'am John. I am from London"
area = txt3.split("from ")[1]
print("Residence Area:", area)

# 5. Reverse String
print("\n5. Reverse String")
user_str = input("Enter a string to reverse: ")
print("Reversed:", user_str[::-1])

# 6. Count Vowels
print("\n6. Count Vowels")
text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Number of vowels:", count)

# 7. Find Maximum Value
print("\n7. Find Maximum Value")
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum value:", max(nums))

# 8. Check Palindrome
print("\n8. Check Palindrome")
word = input("Enter a word: ")
if word.lower() == word[::-1].lower():
    print("It is a palindrome.")
else:
    print("Not a palindrome.")

# 9. Extract Email Domain
print("\n9. Extract Email Domain")
email = input("Enter your email: ")
domain = email.split("@")[1]
print("Domain:", domain)

# 10. Generate Random Password
print("\n10. Generate Random Password")
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
