import unittest

class Main(object):
    def add(self, x:int,y:int):
        return x+y

class UnitTestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Main().add(5,5), 10)
    

if __name__ == "__main__":
    unittest.main()

