class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        word1_sum=""
        word2_sum=""
        for i in range(len(word1)):
            word1_sum +=word1[i]
        
        for j in range(len(word2)):
            word2_sum +=word2[j]

        if word1_sum == word2_sum:
            return True
        else:
            return False