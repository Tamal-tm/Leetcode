class Solution(object):
    def reverseVowels(self, s):
        vols = ['a','e','i','o','u','A','E','I','O','U']
        mylist_vals = []
        mylist_pos = []
        str_word = ""

        # collect vowels and their positions
        for i in range(len(s)):
            if s[i] in vols:
                mylist_vals.append(s[i])
                mylist_pos.append(i)

        # reverse vowels once
        mylist_vals.reverse()

        # convert to list for easy modification
        s_list = list(s)
        for i in range(len(mylist_pos)):
            s_list[mylist_pos[i]] = mylist_vals[i]

        str_word = "".join(s_list)

        return str_word