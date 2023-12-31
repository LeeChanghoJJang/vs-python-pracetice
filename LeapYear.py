def is_leap_year(year):
    if year %4 !=0:
        return False
    elif year %100 !=0:
        return True
    elif year %400 !=0:
        return False
    else:
        return True

print(is_leap_year)
print(is_leap_year(2100))
print(is_leap_year(2008))