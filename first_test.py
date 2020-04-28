# 1

st = "Print only the words that start with s in this sentence"
print("Task #1: Print only the words that start with 's' in this sentence\n")

for word in st.split():
    if word[0].lower() == "s":
        print(word)

# 2
print("\nTask #2: Use range() and print all even numbers from 0 to 10\n")

for number in range(0, 11, 2):
    print(number)

# 3
print("\nTask #3: Use list comprehension to print list of numbers from 1 to 50 that divisible by 3\n")

list_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(list_by_3)

# 4
st = "Print every word in this sentence that has an even number of letters"
print("\nTask #4: Print every word in this sentence that has an even number of letters\n")

for word in st.split():
    if len(word) % 2 == 0:
        print("Word " + "'" + word + "'" + " has even length.")

# 5
print(
    "\nTask #5: Print numbers from 1 to 100, if number divisible by '3' print 'Fizz', if number divisible by '5' print "
    "'Buzz', if number divisible by '3' and '5' print 'FizzBuzz'\n")

for number in range(1, 101):
    if (number % 3 == 0) & (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# 6
st = "Create list of the first letters of every word in this string"
print("\nTask #6: Create list of the first letters of every word in this string\n")

list_of_first_letters = [word[0][0] for word in st.split()]

print(list_of_first_letters)
