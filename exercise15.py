import exercise8

rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직붕붕카: 110cm~140cm'''
def allowedrides(height):
    assert type(height) == int

    result = []
    for ride in rides.splitlines():
        ridename,cmmin,cmmax = exercise8.read(ride)
        if (not cmmin and not cmmax) or (height >= cmmin and not cmmax) or (cmmin <= height <= cmmax):
            result.append(ridename)
    return result

# if __name__ == '__main__':
#     height = int(input())
#     for x in allowedrides(height):
#         print(x)

setlist = []
for heights in input().split():
    setlist.append(set(allowedrides(int(heights))))

print(setlist)
print(set.intersection(*setlist))
for ride in set.intersection(*setlist):
    print(ride)


def read1(text):
    ridename, numbers = map(str.strip,text.split(':'))
    cmmin = cmmax = None
    result =[]
    if '~' in numbers:
        cmmin, cmmax = map(int,numbers.replace('cm','').split('~'))
    elif '이상' in numbers:
        cmmin = int(numbers.split('cm')[0])
    return cmmin, cmmax, ridename

# print(read1('와일드 윙: 140cm ~ 190cm'))

