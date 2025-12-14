class Solution(object):
    def reorderedPowerOf2(self, n):
        s = sorted(str(n))

        for i in range(31):   # 2^0 to 2^30 (covers all int limits)
            if sorted(str(1 << i)) == s:
                return True

        return False
