from collections import deque,Counter
d=deque()
d.append('a')
d.append('b')
d.append('c')
d.appendleft('d')
d.pop()
d.popleft()
d.rotate(1)
print(d)

c = Counter('hello world')
print(c) # dict형태로 각 원소 얼마나 있는지
#Orderdict, defaultdict 잘 사용안됨

# 함수형 프로그래밍 : 순수함수(외부변수를 참조하여 값 생성 불가 + 불변성)
one= 10
def add(a,b):
    return a+b+one
print(add(10,20)) #외부변수 참조안됨

one = [10,20,30]
def change(l):
    l[2]=1000
    return l

change(one) #외부값을 함수안에서 수정안되게끔. one의 값을 카피해서 입력했어야 함. 
# 입력에만 의존해야한다는것
print(one) # 즉 함수형 프로그래밍은 코드의 예측성, 안정성 있음 

# 절차형 프로그래밍 : 프로그램을 일련의 절차 또는 단계로 묘사하는 패러다임. 복잡할 수 있음

# 객체지향 프로그래밍 : 한마디로 클래스라는 템플릿으로 객체를 생성하여 상태와 동작을 정의.
# 코드의 구조를 개선, 복잡성 관리함. 재사용에 유용 

# 일급함수(First-Class-Function) : 프로그래밍 언어가 함수를 일급 시민(값)으로 취급
# 함수를 다른 객체와 동일하게 취급하며, 다음과 같은 동작 가능
hojun = print
hojun('hello world') # - 함수를 변수에 할당
hello = [hojun, hojun, hojun]
hello[0]('빌어먹을') # - 함수를 데이터구조에 저장
def hello(f):
    f('hojun!!')
hello(hojun)# - 함수를 인자로 다른 함수에 전달가능
def hello(f):
    return f
hohojun = hello(hojun)
hohojun('hello!!!')# - 함수를 결과로서 반환가능

# 고차함수 : 다른 함수를 인자로 받거나, 결과로서 함수를 반환하는 함수를 의미 
def apply_to_three(func):
    return func(3)

def square(n):
    return n**2

print(apply_to_three(square)) # 함수 안에 함수를 인자로 넣음 

# 람다함수 : 이름이 없는 일회용 함수. 주로 한줄로 표현

# 클로저 : 함수가 생성된 시점의 범위에 있는 모든 변수를 기억하고 이에 접근가능케 함 
# - 함수 내부에 함수가 정의
# - 내부 함수는 외부 함수의 변수를 참조
# - 외부함수는 내부 함수를 반환

def outer_func(): # 이딴건 클로저가 아님
    def inner_func():
        return 100+100
    return inner_func

def outer_function(x): # 이런게 클로저
    def inner_function(y):
        return x+y  
    return inner_function

inner = outer_function(100)
print(inner(200)) # 데이터 은닉이 좋음, 지연 바인딩 

# 데코레이터 : 고차함수. 하나 이상의 함수를 인자로 받고, 함수를 결과로 반환 

def simple_decorator(function):
    def wrapper():
        print('Before the function call')
        function()
        function()
        function()
        print('After the function call')
    return wrapper

@simple_decorator # 데이터 전처리에 효율적인 사용
def hello():
    print('Hello, World')

hello() # 데코레이터가 없는 상태에서는 simple_decorator(hello)()와 같음

def 전처리(function):
    def wrapper(l):
        print('Before the function call')
        print(function(list(map(int,l))))
        print('After the function call')
    return wrapper
@전처리
def 합(l):
    return sum(l)

print(합([1,2,3,'4']))

def debug1(function):
    def new_function(n):
        print(f'{function.__name__} 함수 시작')
        print(n)
        result = function(n)
        print(f'{function.__name__} 함수 끝')
        return result
    return new_function

def debug2(function):
    def new_function_two(n):
        print(f'{function.__name__} 함수 시작')
        print(n)
        result = function(n)
        print(f'{function.__name__} 함수 끝')
        return result
    return new_function_two

def debug3(function):
    def new_function_three(n):
        print(f'{function.__name__} 함수 시작')
        print(n)
        result = function(n)
        print(f'{function.__name__} 함수 끝')
        return result
    return new_function_three
@debug1
@debug2
@debug3
def sum_1_to_n(n):
    return n * (n+1)/2

result = sum_1_to_n(30)
print(result)

def add(n):
    def decorator(function):
        def new_function(*args,**kwargs):
            result = function(*args,**kwargs)
            return result + n
        return new_function
    return decorator

@add(10)
def plus(a,b):
    return a+b
result = plus(10,20)
print(f'result:{result}')

class Debug:
    def __init__(self,function):
        self.function = function
    
    def __call__(self,*args,**kwargs):
        print(f'{self.function.__name__} 함수시작')
        self.function()
        print(f'{self.function.__name__} 함수 끝')

@Debug
def f1():
    print('안녕하세요')

@Debug
def f2():
    print('hello')

f1()
f2()
# 데코레이터는 함수의 실행시간 측정, 시스템의 로그기록, 사용자의 접근권한 확인 등 여러 일가능