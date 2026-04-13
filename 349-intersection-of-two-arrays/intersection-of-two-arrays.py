class Solution(object):
    def intersection(self, nums1, nums2):
        freq = {}
        result = []

        # Mark elements of nums1
        for num in nums1:
            freq[num] = 1   # just record presence

        # Check nums2 for intersection
        for num in nums2:
            if num in freq and freq[num] == 1:
                result.append(num)
                freq[num] = 0  # avoid duplicates

        return result