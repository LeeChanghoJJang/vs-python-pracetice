import LeapYear
import unittest # 단위테스트 

class TestLeapYear(unittest.TestCase): # Testcase를 상속하는 클래스 생성 
    def test_2020(self): # 반드시 test로 이름 시작해야함 
        r= LeapYear.is_leap_year(2020)
        self.assertEqual(r,True)
    
    def test_2077(self):
        r = LeapYear.is_leap_year(2077)
        self.assertEqual(r,False)

    def test_2000(self):
        r = LeapYear.is_leap_year(2000)
        self.assertEqual(r,True)

if __name__ =='__main__':
    print(unittest.main())
