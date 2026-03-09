class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine=list(magazine)
        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        return True
    
        
        
        