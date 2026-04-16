class Solution(object):
    def checkInclusion(self, s1, s2):
        list_s1 = list(s1)
        list_s2 = list(s2)
        n = len(list_s1)

        # sort once for comparison
        sorted_s1 = sorted(list_s1)

        for i in range(len(list_s2) - n + 1):
            # get each substring of s2 with same length as s1
            random_chars = list_s2[i:i+n]  
            random_word = "".join(random_chars)

            # check if it's a permutation
            if sorted(random_word) == sorted_s1:
                return True
        return False