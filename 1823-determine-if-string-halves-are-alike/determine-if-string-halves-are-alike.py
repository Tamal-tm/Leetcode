class Solution(object):
    def halvesAreAlike(self, s):
        s = s.lower()
        count_1 = 0
        count_2 = 0
        vowels = {'a','e','i','o','u'}   # set is faster than tuple
        n = len(s) // 2

        for i in range(n):
            if s[i] in vowels:
                count_1 += 1
            if s[i + n] in vowels:
                count_2 += 1

        return count_1 == count_2
