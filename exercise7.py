def triple(x):
    return f'{x*3}'
print(triple(3))

from datetime import datetime

def korean_age(x):
    today = datetime.today()
    return today.year - x +1

print(korean_age(1994))

def simple_interest(p,r,t):
    return p*r*t
print(simple_interest(10000000,0.03875,5))

def compound_interest_amount(p,r,t,n):
    return p*(1+r/n)**(n*t)

print(compound_interest_amount(1500000,0.043,6,4))