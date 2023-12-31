def primenumber2(range_num):
    num_list = list(range(2, range_num + 1))
    index = 0
    while index < len(num_list):
        num = num_list[index]
        num_list = list(filter(lambda x: x == num or x % num, num_list))
        print(num_list)
        index += 1
    return num_list

def primenumber3(max_num):
    num=2
    while num <=max_num:
        cnt = 0
        i=1
        while i<=num:
            if num % i ==0:
                cnt +=1
            i+=1
        if cnt ==2:
            print('{0}의 약수가 {1}개이므로 "소수"입니다.'.format(num,cnt))
        num+=1
        
def primenumber4(num):
    while True:
        if not num:
            break  # 반복문을 탈출합니다.
        if num < 0:
            print('양의 정수로 입력하시오')
            continue  # 반복문의 처음으로 갑니다.

    i = 2
    flag = True
    while i <= num **0.5:  # 절반까지만 반복
        if num % i == 0:    # 나누어지면 중간에 약수가 있으므로 소수 아님
            flag = False
            break
        i += 1

    if flag:  # flag 값이 참이면 나누어진적이 없다. 즉 소수
        return '{0}은 "소수입니다."'.format(num)
    else:
        return '{0}은 "소수가 아닙니다."'.format(num)

def transfor(num):
    #2진수 변환
    dem=''
    while num:
        num,d = divmod(num,2)
        dem+=str(d)
    return ''.join(dem[::-1])

def transfor1(num):
    arr=[]
    while num:
        num,d = divmod(num,2)
        arr.insert(0,d)
    return ''.join(map(str,arr))
print(transfor(134))
print(transfor1(134))

def cal_date():
    years,months,days =map(int,input().split(' '))
    return f'{months}/{days:02d}/{years}'

def read_date():
    year, month, day = tuple(map(int, input().split()))
    return year, month, day

def print_date(date):
    year, month, day = date
    print("%02d/%02d/%04d" % (month, day, year))

def advance_day(date):
    year, month, day = date
    
    end_of_month = (month, day) in [(1, 31), (2, 28), (3, 31), (4, 30), (5,
        31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    
    end_of_year = month == 12 and day == 31
    
    if end_of_month:
        if end_of_year:
            year += 1
            month = 1
            day = 1
        else:
            month += 1
            day = 1
    else:
        day += 1
    
    return year, month, day
    
if __name__ == "__main__":
    today = read_date()
    print_date(today)
    tomorrow = advance_day(today)
    print_date(tomorrow)


