def multi(num):
    for i in range(1,10):
        print(f'{num} * {i} = {num*i}')

if __name__ == '__main__':
    for i in range(2, 10):
        multi(i)
        print()