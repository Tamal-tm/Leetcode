class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            # only start counting at the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                count = 1
                while current + 1 in num_set:
                    current += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count
