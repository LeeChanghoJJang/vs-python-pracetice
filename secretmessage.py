# message = open('postcard.txt',encoding='UTF-8')
# a=''
# for i in message.readlines()[3:9]:
#     for j in i.strip().replace('.','').replace(',','').replace(':','').upper().split()[:2]:
#         a+=j+' '
# print(a)

#1
txt= open('postcard.txt','r').read()
print('*** 1. Full Text ***'+ txt + '\n')

#2
head, body, tail = tuple(txt.split('\n\n'))
print('*** 2. Body ***\n' + body + '\n')

#3
import re
s = re.sub(r'[:,\.]','',body)
print('*** 3. Text without Punctuation ***\n' + s + '\n')

#4
s= s.upper()
print('*** 4. Uppercase ***\n' + s + '\n')

#5 
secret_words = []
for line in s.split('\n'):
    secret_words += line.split()[:2]

message = ' '.join(secret_words)
print(message)