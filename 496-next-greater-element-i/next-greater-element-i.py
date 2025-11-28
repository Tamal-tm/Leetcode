class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        mylist = []
        max_value = max(nums2)
        max_length = len(nums2) - 1

        for i in range(len(nums1)):
            if nums1[i] == max_value:
                mylist.append(-1)
            else:
                value = nums2.index(nums1[i])

                # search for the next greater element to the RIGHT
                next_greater = -1
                for j in range(value + 1, len(nums2)):
                    if nums2[j] > nums1[i]:
                        next_greater = nums2[j]
                        break

                mylist.append(next_greater)

        return mylist
