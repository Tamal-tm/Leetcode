class Solution(object):
    def halvesAreAlike(self, s):
        s=s.lower()
        count_1=0
        count_2=0
        vowels=('a','e','i','o','u')
        first_half=s[:len(s)//2]
        second_half=s[(len(s)//2):]
        for i in range(len(first_half)):
            if first_half[i] in vowels:
                count_1 +=1
            if second_half[i] in vowels:
                count_2 +=1
        if count_2 == count_1:
            return True
        else:
            return False
                
        
        