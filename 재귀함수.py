def hap(a,b):
    return a+b

def gop(a,b):
    return a*b

def hap_gop(a,b):
    return hap(a,b), gop(a,b)

def countdown(n):
    if n==0:
        print('Blastoff')
    else:
        print(n)
        return countdown(n-1)

countdown(10)

def 복리계산(price,이율,복리횟수,기간):
    if 기간 >0:
        price *= (1+이율/복리횟수) ** (복리횟수)
        기간-=1
        return 복리계산(price,이율,복리횟수,기간)
    else:
        return price
    
print(복리계산(1500000,0.043,6,1/2))
print(1500000*(1+0.043/6)**24)