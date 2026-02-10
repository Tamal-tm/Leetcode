class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        result = []

        for x in set1:
            if x in set2 or x in set3:
                result.append(x)

        for x in set2:
            if x in set3 and x not in result:
                result.append(x)

        return result
