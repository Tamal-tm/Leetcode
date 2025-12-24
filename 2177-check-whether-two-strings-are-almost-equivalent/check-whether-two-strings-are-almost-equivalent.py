class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        seen_1 = {}
        seen_2 = {}

        for i in range(len(word1)):
            if word1[i] in seen_1:
                seen_1[word1[i]] += 1
            else:
                seen_1[word1[i]] = 1
        
        for j in range(len(word2)):
            if word2[j] in seen_2:
                seen_2[word2[j]] += 1
            else:
                seen_2[word2[j]] = 1
                
        for key in seen_1:
            if abs(seen_1.get(key, 0) - seen_2.get(key, 0)) > 3:
                return False
        
        for key in seen_2:
            if abs(seen_2.get(key, 0) - seen_1.get(key, 0)) > 3:
                return False
        
        return True
