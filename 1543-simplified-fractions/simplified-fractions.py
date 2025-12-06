class Solution(object):
    def simplifiedFractions(self, n):
        mylist = []
        a = 0   # you used it for shifting start of i
        c = 0   # flag to mark "has common divisor"

        for j in range(1, n):
            
            for i in range(2 + a, n + 1):

                # check gcd(j, i)
                def gcd(x, y):
                    bx = min(x, y)
                    for b in range(2, bx + 1):
                        if x % b == 0 and y % b == 0:
                            return True   # common divisor found
                    return False

                if gcd(j, i):   # if not simplified
                    c = 0       # reset flag, skip
                else:
                    new_item = str(j) + "/" + str(i)
                    mylist.append(new_item)

            a += 1   # keep your structure

        return mylist