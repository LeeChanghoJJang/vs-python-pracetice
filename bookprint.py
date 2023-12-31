import bookstore 

b= bookstore.book('내가 먹었지롱','200원','미니')
b.setData('누가 내 치즈를 먹었을까','300원','미키')
b.printData()
b.__del__()

b=bookstore.book('아프지만 청춘이다','10,000원','법륜스님')
b.setData('그대를 사랑합니다','1,000원','이순재')
b.printData()

# from importlib import reload
# reload(bookstore)