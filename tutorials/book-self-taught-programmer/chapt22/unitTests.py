import unittest
from palindrome import isPalindrome


class TestAlgorirthms(unittest.TestCase):

    def test_isPalindrome(self):
        self.assertEqual(isPalindrome(""), True)
    def test_isPalindrome1(self):
        self.assertEqual(isPalindrome([]), True)
    def test_isPalindrome2(self):
        self.assertEqual(isPalindrome(" "), True)
    def test_isPalindrome3(self):
        self.assertEqual(isPalindrome([0]), True)
    def test_isPalindrome4(self):
        self.assertEqual(isPalindrome("1,1,00,1,1"), True)
    def test_isPalindrome5(self):
        self.assertEqual(isPalindrome([1,1,10,1,1]), True)
    def test_isPalindrom6(self):
        self.assertEqual(isPalindrome("1,1,10,1"), False)
    def test_isPalindrome7(self):
        self.assertEqual(isPalindrome([1,1,10,1]), False)


if __name__ == '__main__':
    unittest.main()
