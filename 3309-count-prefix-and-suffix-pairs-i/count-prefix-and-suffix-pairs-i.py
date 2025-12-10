class Solution(object):
    def countPrefixSuffixPairs(self, words):
        count = 0
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                pref = words[i]
                w = words[j]

                # check if words[i] is both prefix and suffix of words[j]
                if w.startswith(pref) and w.endswith(pref):
                    count += 1
        
        return count
