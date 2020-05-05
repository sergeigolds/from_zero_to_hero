print('\n#1\n')


def gensquares(n):
    for i in range(n):
        yield i ** 2


for i in gensquares(10):
    print(i)

print('\n#2\n')
import random


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)

print('\n#3\n')

s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
