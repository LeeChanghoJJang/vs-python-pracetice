#시저 암호
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase[3:] + string.ascii_uppercase[:3])
tt = str.maketrans(string.ascii_lowercase,string.ascii_uppercase[3:]+string.ascii_uppercase[:3])
print(tt)
print(ord('a'),ord('D'))
print('traue nie dem brutus'.translate(tt))