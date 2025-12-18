class Solution(object):
    def halvesAreAlike(self, s):
        s = s.lower()
        vowels = {'a','e','i','o','u'}
        mid = len(s) // 2
        count_1 = 0
        count_2 = 0

        for i in range(mid):
            if s[i] in vowels:
                count_1 += 1
            if s[i + mid] in vowels:
                count_2 += 1

        return count_1 == count_2
