# with open('ko_en.txt') as f:
#     voca=f.readlines()
# arr=[]

# for i in voca:
#     arr.append(i.strip().split('\t'))

# import random

# def 영어퀴즈():
#     print('Write the following sentence in English.')
#     a= random.choice(arr)
#     print(a[0])
#     ans= input()
#     if ans == a[1]:
#         print('result:Correct!')
#     else:
#         print(f'result:Not correct!\n right answer:{a[1]}')
# 영어퀴즈()

import random

d=dict()

with open('ko_en.txt') as f:
    for line in f.readlines()[1:]:
        k,v = tuple(line.split('\t'))
        d[k]=v

quiz = list(d.keys())
random.shuffle(quiz)

while True:
    if len(quiz) ==0:
        break

    q= quiz.pop()
    print('Write the following sentence in English')
    print(q)
    a= input('\nyour answer: ')

    if a== d[q].rstrip():
        print('\nresult: Correct!')
    else:
        print('\nresult: Not correct!')
        print('right answer:'+d[q].rstrip()+'\n')

    input()

    print('-'*80)