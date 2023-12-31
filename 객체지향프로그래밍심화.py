class MyClass:
    count=0

    @classmethod
    def increment(cls):
        cls.count+=1

MyClass.increment()
print(MyClass.count)

class CompletionList:
    def __init__(self):
        self.subject_list=[]
    
    def show(self):
        print(self.subject_list)
    
    def append(self,subject):
        self.subject_list.append(subject)

    @staticmethod
    def academic_warning(subject):
        '''
        내부에서 클래스 변수, 인스턴스 변수 수정하는 것이 가능하지 않습니다.
        '''
        return abs(1.5 - subject['grades'])

c= CompletionList()
subject1 = {'name':'Python','grades':2.5}
subject2 = {'name':'HTML/CSS','grades':3.5}

c.append(subject1)
c.append(subject2)
print(c.academic_warning(subject2))

class Person:
    def __init__(self,first_name,last_name):
        self._first_name = first_name
        self._last_name=last_name

    @property 
    def full_name(self):
        return f'{self._first_name} {self._last_name}'
    
hojun = Person('lee','hojun')
print(hojun._first_name, hojun._last_name)
print(hojun.full_name) # property 속성접근자는 리턴값을 내부에 있는 변수처럼 출력가능
# 만약 property 없으면 full_name 함수 호출 해야함 

class Duck: # 이 코드에서는 obj가 실제로 Duck 타입인지 상관안하고 quack메서드 호출 
    def quack(self): # 덕타이핑
        print('Quack!')

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def quack(obj): # obj가 Duck 타입이든 아니든 상관 안함 
    obj.quack()

duck = Duck()
person = Person()
quack(duck)
quack(person)

# 추상클래스
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass

class Person(AbstractClassExample): # 추상클래스는 인스턴스로 만들 수 없음 
    def __init__(self,name):
        self.name = name
    
    def print_name(self):
        print(f'제 이름은 {self.name}입니다.')
# 연산자 오버라이딩 : 부모 클래스에서 정의한 메소드를 자식 메소드에서 변경하는 것
# 연산자 오버로딩 : 동일한 이름의 함수를 매개변수에 따라 다른기능으로 동작(파이썬 미허용)
    def do_something(self): 
        pass

hojun = Person('hojun')
hojun.print_name()

class Cal:
    def add(a):
        pass

    def add(a,b):
        pass

    def add(a,b,c):
        pass
c=Cal()
c.add(10)
c.add(10,20)
c.add(10,20,30)

# 인터페이스 : 객체가 어떤 메서드를 구현해야 하는지 정의. python은 내장키워드 없음
from abc import ABC, abstractmethod

class MyInterface(ABC):
    
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass