# 1
def lesser_of_two_events(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_events(2, 4))
print(lesser_of_two_events(2, 5), '\n')


# 2
def animal_crackers(text):
    word_list = text.lower().split()

    return word_list[0][0] == word_list[1][0]


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers('Crazy Kangaroo'), '\n')


# 3
def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3), '\n')


# 4
def old_macdonald(name):
    return name[:3].capitalize() + name[3:].capitalize()


print(old_macdonald('macdonald'), '\n')


# 5
def master_yoda(text):
    result = text.split()[::-1]
    return ' '.join(result)


print(master_yoda('I am home'))
print(master_yoda('We are ready'), '\n')


# 6
def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209), '\n')


# 7
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]), '\n')


# 8
def paper_doll(text):
    result = ''

    for char in text:
        result += char * 3

    return result


print(paper_doll('Hello'))
print(paper_doll('Mississippi'), '\n')


# 9
def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in ([a, b, c]) and sum([a, b, c]) - 10 <= 21:
        return sum([a, b, c]) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11), '\n')


# 10
def summer_69(arr):
    total = 0

    for n in arr:
        if n == 6 or n == 7 or n == 8 or n == 9:
            continue
        else:
            total = total + n

    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]), '\n')


# 11
def spy_game(nums):
    code = [0, 0, 7, 'x']

    for n in nums:
        if n == code[0]:
            code.pop(0)

    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]), '\n')


# 12
def count_primes(num):
    prime_numbers = []

    for n in range(2, num + 1):
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            prime_numbers.append(n)

    return len(prime_numbers)


print(count_primes(100))
