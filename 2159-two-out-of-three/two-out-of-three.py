class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        mylist=[]
        n_nums1=nums1
        n_nums2=nums2
        n_nums3=nums3
        for i in range(len(n_nums1)):
            if n_nums1[i] in n_nums2 and n_nums1[i] not in mylist:
                mylist.append(n_nums1[i])
            elif n_nums1[i] in n_nums3 and n_nums1[i] not in mylist:
                mylist.append(n_nums1[i])

        for i in range(len(n_nums2)):
            if n_nums2[i] in n_nums3 and n_nums2[i] not in mylist:
                mylist.append(n_nums2[i])
            elif n_nums2[i] in n_nums1 and n_nums2[i] not in mylist:
                mylist.append(n_nums2[i])
        
        return mylist
