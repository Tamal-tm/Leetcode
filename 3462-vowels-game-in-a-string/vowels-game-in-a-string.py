class Solution(object):
    def doesAliceWin(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for char in s:
            if char in vowels:
                return True

        return False