class Solution(object):
    def countSmaller(self, nums):
        # Assign a rank to each unique number
        sorted_unique = sorted(set(nums))
        rank = {num: i for i, num in enumerate(sorted_unique)}
        size = len(sorted_unique)
        
        # Fenwick Tree (BIT) for prefix sums
        BIT = [0] * (size + 1)
        
        def update(i):
            i += 1  # BIT is 1-indexed
            while i <= size:
                BIT[i] += 1
                i += i & -i
        
        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += BIT[i]
                i -= i & -i
            return s
        
        res = []
        for num in reversed(nums):
            r = rank[num]
            res.append(query(r - 1))  # count of smaller numbers
            update(r)                  # mark current number seen
        
        return res[::-1]