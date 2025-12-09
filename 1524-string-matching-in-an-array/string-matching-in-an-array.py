class Solution(object):
    def stringMatching(self, words):
        mylist=[]
        length=len(words)
        
        for i in range(0,length):
            for word in words:
                big_word = max(words, key=len)
                if word in big_word and word not in mylist and word!=big_word:
                    mylist.append(word)
            words.remove(big_word)
        return (mylist)
            