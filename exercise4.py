num = int(input())
result=''
if num %400==0:
    result ='윤년'
elif num%100==0:
    result= '평년'
elif num%4==0:
    result = '윤년'
else:
    result='평년'
print(f'{result}입니다')