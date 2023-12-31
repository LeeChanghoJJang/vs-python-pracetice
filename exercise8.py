# print(list(map(lambda x: x ** 2, range(5))))
# print((lambda x,y: x + y)(10, 20))

# from functools import reduce

# print(reduce(lambda x,y:x+y,[0,1,2,3,4]))
# print(reduce(lambda x,y:y+x,'abcde'))
# print(list(filter(lambda x:x%2==1,range(10))))

def read(text):
    ridename,limit = map(str.strip,text.split(':'))
    cmmin = cmmax =None
    if '~' in limit:
        templist=[]
        for x in limit.split('~'):
            templist.append(x.replace('cm',''))
        cmmin,cmmax = int(templist[0]),int(templist[1])
    elif '이상' in limit:
        cmmin = int(limit.split('cm')[0])
    return ridename, cmmin,cmmax

# if __name__ == '__main__':
#     ridename, cmmin, cmmax = read(input())
#     print("이름:", ridename)
#     print("하한:", cmmin)
#     print("상한:", cmmax)
