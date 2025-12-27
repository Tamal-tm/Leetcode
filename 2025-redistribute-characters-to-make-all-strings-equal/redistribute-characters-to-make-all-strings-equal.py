class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words) <= 1:
            return True
        count = {}
        for word in words:
            for char in word:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] = count[char] + 1

        for val in count.values():
            if val%len(words) != 0:
                return False
        
        return True