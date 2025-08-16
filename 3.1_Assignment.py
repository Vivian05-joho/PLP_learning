# 1. Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.

# Step 1: Ask the user how many integers they want to enter
count = int(input("How many integers do you have? "))

# Step 2: Create an empty list to store the numbers
numbers = []

# Step 3: Loop to collect the numbers one by one
for i in range(count):
    num = int(input(f"Input number {i+1}: "))  # i+1 makes it say "1, 2, 3..." instead of 0
    numbers.append(num)

total_sum = sum(numbers)
print(f"The sum of the numbers is {total_sum}")

# 2________________________________________________________________________
books = ("Rich Dad", "Poor Dad", "Extremist")

for book in books:
    print(book)

# 3____________________________________________________________________________
# Create an empty dictionary
person = {}

# Ask the user for information
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print(person)

# 4____________________________________________________________________
person = {}

# Ask the user for information
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print(person)

# 5____________________________________________________________________________
# First set
set1 = set(map(int, input("Enter numbers for the first set (separated by spaces): ").split()))
# Second set
set2 = set(map(int, input("Enter numbers for the second set (separated by spaces): ").split()))
# Common elements
common = set1 & set2   # or use set1.intersection(set2)
print("Common elements:", common)

#6_________________________________________________________________________________
# Step 1: make a list of words
words = ["apple", "cat", "banana", "dog", "grape"]
# Step 2: use list comprehension to keep only words with odd length
odd_words = [word for word in words if len(word) % 2 != 0]
# Step 3: print the result
print("Words with odd number of characters:", odd_words)