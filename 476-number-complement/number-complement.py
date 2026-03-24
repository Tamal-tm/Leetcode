class Solution(object):
    def findComplement(self, num):
        binary_string_without_prefix = bin(num)[2:]
        str_word = ""
        a = str(binary_string_without_prefix)

        for i in range(len(a)):
            if a[i] == '0':
                str_word += "1"
            elif a[i] == '1':
                str_word += "0"

        # Convert binary string back to integer
        result = int(str_word, 2)
        return result