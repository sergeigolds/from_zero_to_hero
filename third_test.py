# 1
from math import pi, pow


def vol(rad):
    return 0.75 * pi * pow(rad, 3)


print(vol(2), '\n')


# 2
def ran_check(num, low, high):
    if num in range(low, high + 1):
        print(str(num) + ' is in range between ' + str(low) + ' and ' + str(high))
    else:
        print("The number is outside the given range.")


ran_check(5, 2, 7)


def ran_bool(num, low, high):
    return num in range(low, high + 1)


print(ran_bool(5, 2, 7), '\n')


# 3
def up_low(st):
    is_lower = 0
    is_upper = 0

    for letter in st:
        if letter.islower():
            is_lower += 1
        elif letter.isupper():
            is_upper += 1

    print('Original String : ' + str(st))
    print('No. of Upper case characters : ' + str(is_upper))
    print('No. of Lower case characters : ' + str(is_lower), '\n')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# 4
def unique_list(lst):
    uniq = []

    for num in lst:
        if num not in uniq:
            uniq.append(num)
    print('Sample List: ' + str(lst))
    print('Unique List: ' + str(uniq), '\n')


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


# 5
def multiply(numbers):
    total = 1

    for num in numbers:
        total = total * num
    return total


print(multiply([1, 2, 3, -4]), '\n')


# 6
def palidnrome(s):
    reversed_s = s[::-1]

    return s == reversed_s


print(palidnrome('helleh'), '\n')

# 7
import string

alphabet = string.ascii_lowercase


def ispangram(st):
    my_list = []

    for letter in st:
        if letter not in my_list and letter != ' ':
            my_list.append(letter.lower())

    my_list.sort()
    sorted_list = ''.join(my_list)

    return sorted_list == alphabet


print(ispangram('The quick brown fox jumps over the lazy dog'))
