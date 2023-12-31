# # Syntax Error : 문법오류
# for i in range(10):
#     if 0 and (1/0): #zeroDivisionerror 일어나지 않음 뒤에꺼 안읽음 앞에가 false라
#         print(i)
#     print(i)

# # Name Error 생략.
# # Index Error 
# my_list = [1,2,3]
# print(my_list[3:]) # 슬라이싱은 에러 반환 안함

# # Key Error 
# my_dict = {'a':1,'b':2}
# print(my_dict['c']) # --> Key Error
# print(my_dict.get('c','없음'))

# # ValueError 
# int('a')

# # ZeroDivisionError
# x=10
# y=0
# print(x/y)

# #Attribute Error
# my_list = [1,2,3]
# print(my_list.appeend(4)) # append를 못찾음

# #Type Error
# def add(x,y):
#     return x+y
# add(1,2,3) # 인자 개수에러는 메서드에 전달된 인자의 개수가 맞지 않을 때 발생

# #file I/O Error
# f = open('non-existent.txt','r')
# f.read()  # 파일이 존재하지 않을 때.

# # try : 예외가 발생할 가능성이 있는 코드
# # except : 예외 처리 코드 
# # else : 예외가 발생하지 않을 때 실행되는 코드

# # try : 예외가 발생할 가능성이 있는 코드
# # except: 예외처리 코드
# # finally : 예외 발생 여부와 상관없이 항상 실행되는 코드

# # assert : 가정설정문. 내가 설정한 조건에 만족하지 않는 경우 error 발생

# test = 'hello'

# assert test =='hello','에러 메시지 1'
# assert test =='world','에러 메시지 2'

# 에러 발생시키기 raise 이용

# for i in range(10):
#     if i ==5:
#         raise ValueError('에러입니다')
#     print(i) # 아무것도 없을 때는 RuntimeError


# class Leehojun(Exception):
#     def __init__(self):
#         super().__init__('입력된 값이 leehojun이 아닙니다')

# raise Leehojun

import logging
# logging.basicconfig(level=logging.INFO) # 어느 레벨부터 로깅할지, 기본으로 warning부터

# logging.debug('This is a debug message') # 고쳐야 할 코드, 기록 필요
# logging.info('This is an info message') # 정보성 메시지
# logging.warning('This is a warning message') # 경고 메시지
# logging.error('This is an error message') # 에러 메시지(프로그램은 동작)
# logging.critical('This is a critical message') # 프로그램 중지(에러처리 안된 경우)

import logging.handlers

def logger():
    log_obj = logging.getLogger('log_name') # log name으로 log 객체 생성
    log_obj.setLevel(logging.DEBUG) # 어디부터 기록할지 설정

    fileHandeler = logging.FileHandler(filename='./test.txt') # 파일로 기록
    streamHandler = logging.StreamHandler() # 콘솔에 출력

    fileHandeler.setLevel(logging.INFO) # 파일 기록 레벨 설정
    streamHandler.setLevel(logging.DEBUG) # 콘솔 기록 레벨 설정
    
    formatter = logging.Formatter('%(name)s, %(asctime)s,%(levelname)s,%(message)s')
    # 포맷 생성
    fileHandeler.setFormatter(formatter) #파일 메세지 포멧 설정
    streamHandler.setFormatter(formatter)
    
    log_obj.addHandler(fileHandeler) # log_obj handler에 파일 출력 방식 추가
    log_obj.addHandler(streamHandler) # log_obj handler에 콘솔 방식 추가

    return log_obj

log = logger()

# 아래 코드를 기록하고 싶은 곳에 함께 설정

log.debug('debug')
log.info('info')
log.warning('warning')
log.error('error')
log.critical('critical')

print('---')

# 아래와 같이 사용
def f():
    try:
        x=1/0
    except Exception as e:
        print(e)
        log.error(f'{e} error')

f()