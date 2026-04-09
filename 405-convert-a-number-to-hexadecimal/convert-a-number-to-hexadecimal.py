class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32  # convert negative to 32-bit unsigned form
        
        hex_str = ""
        chars = "0123456789abcdef"
        
        while num > 0:
            hex_str = chars[num % 16] + hex_str
            num //= 16
        
        return hex_str