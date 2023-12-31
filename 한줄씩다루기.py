import os
# letter = open('C:/Users/User/Desktop/test/vs-python/letter.txt','a+')
# letter.write('I"m fine. Thank you. and you?')
# letter.close()
license= open('C:/Users/User/AppData/Local/Programs/Python/Python311/LICENSE.txt')
# print(os.getcwd())
# print(os.listdir())

# for x in range(5):
#     print(license.readline())
lines = license.readlines()
print()
for i in lines[-10:]:
    print(i,end='')
