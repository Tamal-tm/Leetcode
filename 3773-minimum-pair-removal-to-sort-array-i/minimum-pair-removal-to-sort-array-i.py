class Solution(object):
    def minimumPairRemoval(self, nums):
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        count = 0
        arr = nums[:]

        while not is_sorted(arr):
            min_sum = float("inf")
            idx = 0

            for i in range(len(arr) - 1):
                if arr[i] + arr[i + 1] < min_sum:
                    min_sum = arr[i] + arr[i + 1]
                    idx = i

            merged = arr[idx] + arr[idx + 1]
            arr.pop(idx)
            arr.pop(idx)
            arr.insert(idx, merged)

            count += 1

        return count
