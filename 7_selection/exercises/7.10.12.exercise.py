'''
3 criteria must be taken into account to identify leap years:
    The year is evenly divisible by 4;
    
    If the year can be evenly divided by 100, it is NOT a leap year, unless;
    
    The year is also evenly divisible by 400. Then it is a leap year.

Write a function that takes a year as a parameter and returns
True if the year is a leap year, False otherwise.
'''


import unittest


def isLeap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
            
    elif year % 4 == 0:
        return True
    
    else:
        return False


class TestIdentifyLeapYear(unittest.TestCase):
    def test_identifyLeapYear(self):
        self.assertEqual(isLeap(2000), True)
        self.assertEqual(isLeap(2004), True)
        self.assertEqual(isLeap(2008), True)
        self.assertEqual(isLeap(2012), True)
        self.assertEqual(isLeap(2016), True)
        self.assertEqual(isLeap(2020), True)
        self.assertEqual(isLeap(2024), True)
        self.assertEqual(isLeap(2028), True)
        self.assertEqual(isLeap(2032), True)
        self.assertEqual(isLeap(2036), True)
        self.assertEqual(isLeap(2040), True)
        self.assertEqual(isLeap(2044), True)
        self.assertEqual(isLeap(2048), True)

    def test_falseLeapYear(self):
        self.assertEqual(isLeap(2002), False)
        self.assertEqual(isLeap(2006), False)
        self.assertEqual(isLeap(2010), False)
        self.assertEqual(isLeap(2014), False)
        self.assertEqual(isLeap(2018), False)
        
        self.assertEqual(isLeap(1800), False)
        self.assertEqual(isLeap(1900), False)


if __name__ == '__main__':
    unittest.main()

'''
The complete list of leap years in the first half of the 21st century is
therefore 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036,
2040, 2044, and 2048.
'''
'''
Fail    True    False   Tested isLeap on an input of 1800
Fail    True    False   Tested isLeap on an input of 1900
'''