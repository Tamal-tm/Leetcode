class Solution(object):
    def stringMatching(self, words):
        mylist = []
        length = len(words)

        # Sort once → biggest words at the end
        words.sort(key=len)

        # Same structure: use nested loops, use big_word each round
        for i in range(length):
            big_word = words[-1]          # largest remaining
            for word in words[:-1]:       # check only smaller words
                if word in big_word and word not in mylist:
                    mylist.append(word)
            
            words.pop()                   # remove big_word (same structure)
        
        return mylist
