class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False  # Negative numbers can't be palindromes

        stack = []
        num = x  # Keep original number (since we'll divide x)

        while x > 0:
            stack.append(x % 10)
            x //= 10

        return stack == stack[::-1]
