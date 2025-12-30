class Solution(object):
    def countDistinctIntegers(self, nums):
        seen = set(nums)

        for n in nums:
            rev = int(str(n)[::-1])
            seen.add(rev)

        return len(seen)
