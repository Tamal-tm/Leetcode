class Solution(object):
    def replaceWords(self, dictionary, sentence):
        mylist = []
        dict_list = sentence.split()
        dictionary.sort(key=len)  # ensure shortest root first
        
        for i in range(len(dictionary)):
            for j in range(len(dict_list)):
                # check if the word starts with the root (not just contains)
                if dict_list[j].startswith(dictionary[i]):
                    dict_list[j] = dictionary[i]
        
        word = " ".join(dict_list)
        return word