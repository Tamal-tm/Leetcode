class Solution(object):
    def calculate(self, s):
        i = 0
        res = 0
        prev = 0
        cur_op = '+'

        while i < len(s):
            ch = s[i]
            if ch == ' ':
                i += 1
                continue

            if ch.isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    cur = cur*10 + int(s[i])
                    i += 1

                if cur_op == '+':
                    res += cur
                    prev = cur
                elif cur_op == '-':
                    res -= cur
                    prev = -cur
                elif cur_op == '*':
                    res -= prev
                    res += prev * cur 
                    prev = prev * cur
                elif cur_op == '/':
                    res -= prev
                    # ensure truncation toward zero
                    if prev >= 0:
                        prev = prev // cur
                    else:
                        prev = -(-prev // cur)
                    res += prev
                continue

            cur_op = ch
            i += 1

        return res

print(Solution().calculate("14-3/2"))   # 13
print(Solution().calculate("3+2*2"))    # 7
print(Solution().calculate("14+2*3-6/2")) # 17
        