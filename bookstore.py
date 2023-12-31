class book:
    def setData(self,title,price,author):
        self.title = title
        self.price = price
        self.author = author
    
    def printData(self):
        print('제목:',self.title)
        print('가격:',self.price)
        print('저자:',self.author)
    
    def __init__(self,title,price,author):
        self.setData(title,price,author)
        print('책을 새로 샀습니다!')
        print(f'제목은 {title}이며, 가격은 {price}입니다')

    def __del__(self):
        del self