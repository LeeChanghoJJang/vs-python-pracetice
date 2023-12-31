def korean_number(num):
    _자리수 = {0:'',1:'일',2:'이',3:'삼',4:'사',5:'오',6:'육',7:'칠',8:'팔',9:'구'}
    k,v= divmod(num,10)
    try:
        if len(str(num)) ==2:
            if k==1:
                return f'십'+ f'{_자리수[v]}'
            else:
                return f'{_자리수[k]}십'+ f'{_자리수[v]}'
        elif len(str(num)) ==1:
            return _자리수[v] if v !=0 else '영'
        elif num==100:
            return '백'
    except:
        print('0~100값을 입력해주세요')        
    
print(korean_number(10))