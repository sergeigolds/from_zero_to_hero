try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print('Error')

try:
    x = 5
    y = 0

except:
    print('Error')

finally:
    print('All done')


def ask():
    while True:
        try:
            number = int(input('Please insert a number: '))

        except:
            print('This is not a number, try again!\n')
            continue

        else:
            break
    print('\nThanks. Square of number: ' + str(number ** 2))


ask()
