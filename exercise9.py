def palindrome(text):
    text = text.lower().replace(' ','')
    return text == text[::-1]
print(palindrome('My gym'))

def sumOfDigits1(num):
    cnt=0
    while num:
        cnt+= num%10
        num//=10 
    return cnt

def sumOfDigits2(num):
    cnt=0
    for i in str(num):
        cnt+=int(i)
    return cnt

print(sumOfDigits1(643))
print(sumOfDigits2(643))

def stem_leaf():
    stem_leafs = [[],[],[]]
    stem_leafs[0]= [0,0,2,4,7,7,9]
    stem_leafs[1]= [1,1,3,8]
    stem_leafs[2]= [0]
    for i in range(len(stem_leafs)):
        print(f'{i}:{stem_leafs[i]}')
print(stem_leaf())

score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]
stem_leaf = [[], [], []]
for s in score:
    d, m = divmod(s, 10)
    stem_leaf[d].append(m)
    print(d,m)

def sumOfDigit3(digit):
    return sum([int(i) for i in str(digit)])
print(sumOfDigit3(47253))

def sumOfDigits4(digit):
    digits = map(int, list(str(num)))
    return sum(digits)

def primenumber(n):
    L=list(range(2,n+1))
    L2=L[:]
    for p in L:
        for q in L:
            if (q in L2) and (q !=p and q%p==0):
                L2.remove(q)
    print(L2)
primenumber(30)

def primenumber2(range_num):
    num_list = list(range(2, range_num + 1))
    index = 0
    while index < len(num_list):
        num = num_list[index]
        num_list = list(filter(lambda x: x == num or x % num, num_list))
        index += 1
    return num_list

print(primenumber2(30))

