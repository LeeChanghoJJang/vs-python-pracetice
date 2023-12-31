# a= [{1,3,2,6,7},{4,5,6,7},{6,7,8,9,1}]
# print(set.intersection(*a))

import random

# print(random.random())
# print(random.randrange(1,7))

# abc = ['a','b','c','d','e','f']
# random.shuffle(abc)
# print(abc)
# print(random.choice(abc))

색깔 = ['빨간','노란','검은','화이트','파란','누런','시퍼런','시뻘건','뽀얀']
음식 = ['소보로','콰삭칩','쭈꾸미','커피','옹심이','고기']
print(random.choice(색깔), random.choice(음식))

import string
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
alpha = string.ascii_letters + string.digits
print(len(alpha))
print(random.choice(alpha))
cnt=''
len_alphabet=10
len_digit = 4
len_special = 2
letters = list()
for i in range(len_alphabet):
    letters.append(random.choice(string.ascii_letters))
    
for i in range(len_digit):
    letters.append(random.choice(string.digits))

for i in range(len_special):
    letters.append(random.choice('`!@#$%^&*()?'))

random.shuffle(letters)
print(''.join(letters))