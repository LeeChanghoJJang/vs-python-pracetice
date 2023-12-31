# class User:
#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email
    
#     def __repr__(self):
#         return (f'{self.__class__.__qualname__}{self.id, self.name, self.email}')

# user = User(123,'hojun','hojun@gmail')
# print(user.__repr__())
# print(User)

from dataclasses import dataclass
# __init__ __repr__, __eq__이 자동으로 추가되는 모듈
@dataclass
class User:
    id:int
    name:str
    email:str

user = User(123,'hojun','hojun@gmail')
print(user)

# 딕셔너리 업데이트
x={'key1':'value1'}
y={'key2':'value2','key3':'value3'}
z={'key4':'value4'}
a={**x,**y}
print(a)
#왈러스 연산자
x = (n:=10) * 2
print(x)
print(n)
#왈러스 연산자 활용 사례
def add(a,b):
    return a+b

합 = add(3,5)
if (합 := add(3,5))==8:
    print(합)

n=0
while (n:=n+1) < 10:
    print(n)

# 딕셔너리 컴프리헨션
books = ['python','javascript','html/css']
book_num = [462365,123253,164557]
book_dict = {book:idx for idx, book in enumerate(books)}
book_dict1 = {book:idx for book,idx in zip(book_num,books)}
print(book_dict)
print(book_dict1)

books2 = [('python',1000,'10000원'),('javascript',2000,'12000원'),('html/css',3000,'13000원')]
books3 = {book:cnt*int(price[:-1]) for book, cnt, price in books2}
print(books3)

# 세트 컴프리헨션
odd_set = {x for x in range(10) if x%2 !=0} # 0~9부터 홀수
print(odd_set)

# 제너레이더 컴프리헨션
square_gen = (x**2 for x in range(10)) # range는 0~9까지의 제너레이터

gen = (i for i in range(2,100000000,2)) #제너레이터는 모든값을 저장하지 않고, 담값만 호출
for i,j in zip(range(10),gen): # 그래서 제너레이터는 메모리 낭비가 별로 없음
    print(i,j) 

# 이터레이터 : 값을 차례대로 꺼낼 수 있는 객체
my_list = [1,2,3,4]
my_iter = iter(my_list) # my_list에 __iter__가 호출됩니다.

print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) # for문의 원리 iterater를 계속반복함.

class Myiterator:
    def __init__(self,stop):
        self.currentValue=0
        self.stop = stop
    
    def __iter__(self):
        self.currentValue=0 # 초기화 해줘야 여러번 사용가능
        return self
    
    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration 
        result = self.currentValue
        self.currentValue +=1
        return result

my_iterator = Myiterator(5)

for i in my_iterator: # 한번 순회가 다되서 한번더하면 안됨. 초기화가 안되서그럼
    print(i) # 생성할때 생성자 호출, 이터레이터 사용시 iter 호출, 그다음은 next만 호출 

# 이터레이터는 언패킹도 가능 ex) range
a,b,c,d = range(4)
print(a,b,c,d)

#제너레이터 : 이터레이터의 특별한 종류의 함수

def count_up_to(n):
    count=1
    while count <= n:
        yield count
        count+=1

counter = count_up_to(5)
print(next(counter))
print(next(counter))

# 제너레이터 컴프리헨션에서 사용했었던 문법을 함수형태의 제너레이터로 구현
def count_(): #메모리 부담이 없기에 사용
    count=2
    while True:
        yield count
        count+=2

for i,j in zip(range(10),count_()): #zip, map,filter은 한번 호출되면 그다음 사용안댐
    print(i,j) # 하지만 sorted는 재사용 가능