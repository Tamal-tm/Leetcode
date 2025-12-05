class Solution(object):
    def hasSameDigits(self, s):
        
        def repeat(s):
            str_num = ""          # FIX: must be a string, not int
            count = 0             # FIX: count must be initialized
            
            new_num = str(s)
            for i in range(len(new_num)-1):
                value = (int(new_num[i]) + int(new_num[i+1])) % 10   # FIX: convert to int
                str_num += str(value)     # FIX: string concat, not number
                count += 1

            if count > 2:
                return repeat(str_num)    # FIX: recursive return
            else:
                return str_num
        
        res = repeat(s)

        if res[0] == res[1]:   # FIX: compare first two digits
            return True
        else:
            return False
