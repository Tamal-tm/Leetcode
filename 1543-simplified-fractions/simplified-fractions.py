class Solution(object):
    def simplifiedFractions(self, n):
        mylist = []
        a = 0

        # Proper gcd function (still similar structure)
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        for j in range(1, n):
            for i in range(2 + a, n + 1):
                # Only add if fraction is simplified
                if gcd(j, i) == 1:
                    new_item = str(j) + "/" + str(i)
                    mylist.append(new_item)
            a += 1

        return mylist
