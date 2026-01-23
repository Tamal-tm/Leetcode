class Solution(object):
    def minimumPairRemoval(self, nums):
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        arr = nums[:]   # work on a copy
        count = 0

        while not is_sorted(arr):
            min_sum = float("inf")
            idx = 0

            # find adjacent pair with minimum sum
            for i in range(len(arr) - 1):
                s = arr[i] + arr[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # merge the pair
            arr[idx] = arr[idx] + arr[idx + 1]
            arr.pop(idx + 1)

            count += 1

        return count
