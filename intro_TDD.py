import unittest

def reverseList(arr):
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-(i+1)]
        arr[len(arr)-(i+1)] = temp
    return arr
class ReverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,5,10]), [10,5,1])
    def testTwo(self):
        self.assertEqual(reverseList(["a","b","c","d","e","f"]), ["f","e","d","c","b","a"])
    def testThree(self):
        self.assertEqual(reverseList([True]), [True])
    def testFour(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])

if __name__ == "__main__":
    unittest.main()

def isPalindrome(word):
    word = word.lower()
    for i in range (int(len(word)/2)):
        if word[i] != word[len(word)-(i+1)]:
            return False
#     return True
class isPalindromTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome("racecar"))
    def testTwo(self):
        self.assertFalse(isPalindrome("racbr"))
    def testThree(self):
        self.assertTrue(isPalindrome("m o m"))
    def testFour(self):
        self.assertFalse(isPalindrome("m om"))
    def testFive(self):
        self.assertTrue(isPalindrome("yoalohaholaoy"))
    def testSix(self):
        self.assertTrue(isPalindrome("YoAlohaHolaOy"))
    def testSeven(self):
        self.assertFalse(isPalindrome("Yo Aloha Hola Oy"))

if __name__ == "__main__":
    unittest.main()

def coins(x):
    quarters = int(x / 25)
    dimes = int((x % 25) / 10)
    nickels = int(((x % 25) % 10) / 5)
    pennies = int(((x % 25) % 10) % 5)
    change = [quarters, dimes, nickels, pennies]
    return change
class CoinsTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    def testTwo(self):
        self.assertEqual(coins(1), [0,0,0,1])
    def testThree(self):
        self.assertEqual(coins(5), [0,0,1,0])
    def testFour(self):
        self.assertEqual(coins(10), [0,1,0,0])
    def testFive(self):
        self.assertEqual(coins(25), [1,0,0,0])
    def testSix(self):
        self.assertEqual(coins(32), [1,0,1,2])
if __name__ == "__main__":
    unittest.main()

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

class FactorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)
    def testTwo(self):
        self.assertEqual(factorial(0), 1)
    def testThree(self):
        self.assertEqual(factorial(4), 24)
if __name__ == "__main__":
    unittest.main()