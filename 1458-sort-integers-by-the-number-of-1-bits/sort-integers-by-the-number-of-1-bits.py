class Solution(object):
    def sortByBits(self, arr):
        def key_func(x):
            return (bin(x).count('1'), x)

        return sorted(arr, key=key_func)

        