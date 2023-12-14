# is it a palindrome?

def isPalindrome(sequence):
    if sequence == sequence[::-1]:
        return True
    return False

a = "qwertyytrewq"
b = [1,1,10,1,1]
# print(isPalindrome(a))
# print(isPalindrome(b))