n = int(input('what were your born?: '))
if n <= 1924:
    gen = 'the Greatest Generation.'
elif n<=1945:
    gen = 'the Silent Generation'
elif n<=1964:
    gen = 'baby boomer'
elif n<=1980:
    gen =  'Generation X'
elif n<=1996:
    gen =  'millennial'
else:
    gen = 'Generation Z'
print(f'You\'re {gen}')