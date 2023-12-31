f = open('C:/Users/User/Desktop/test/vs-python/Python_for_Fun.txt') # 새파일 열기
print(f.read())

letter = open('C:/Users/User/Desktop/test/vs-python/letter.txt','w')
letter.write('Dear Father,')
letter.close()
# 원래 있던 데이터 안지워지게끔
letter1 = open('C:/Users/User/Desktop/test/vs-python/letter.txt','a+')
letter1.write('\n\nHow are you?')
letter1.close()