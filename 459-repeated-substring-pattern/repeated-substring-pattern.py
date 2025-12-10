class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        
        # Try substring lengths from 1 to n//2
        for value in range(1, n//2 + 1):

            # Only check if value divides n
            if n % value == 0:

                # Take substring
                substring = s[:value]

                # Repeat it n/value times
                if substring * (n // value) == s:
                    return True

        return False
