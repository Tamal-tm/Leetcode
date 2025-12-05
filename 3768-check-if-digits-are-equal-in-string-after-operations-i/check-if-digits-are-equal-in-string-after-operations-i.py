class Solution(object):
    def hasSameDigits(self, s):

        def repeat(num):
            new_num = str(num)
            result = ""
            count = 0

            for i in range(len(new_num) - 1):
                value = (int(new_num[i]) + int(new_num[i+1])) % 10
                result += str(value)
                count += 1

            if count > 2:
                return repeat(result)
            else:
                return result

        res = repeat(s)
        return res[0] == res[1]
