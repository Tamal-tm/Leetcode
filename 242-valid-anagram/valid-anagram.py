class Solution(object):
    def isAnagram(self, s, t):
        # If lengths differ, they can’t be anagrams
        if len(s) != len(t):
            return False

        # Check if sorted versions are equal
        if sorted(s) == sorted(t):
            return True
        else:
            return False

        