class Solution(object):
    def numOfPairs(self, nums, target):
        count = Counter(nums)
        ret=0

        for s in nums:
            if target.startswith(s):
                suffix = target[len(s):]
                if suffix in count:
                    ret+=count[suffix]
                    if suffix==s:
                        ret-=1
        return ret