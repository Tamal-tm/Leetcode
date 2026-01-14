# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        mylist = []

        prev = head
        temp = head.next
        count = 2

        while temp.next:
            if (temp.val > prev.val and temp.val > temp.next.val) or \
               (temp.val < prev.val and temp.val < temp.next.val):
                mylist.append(count)

            prev = temp
            temp = temp.next
            count += 1

        if len(mylist) < 2:
            return [-1, -1]

        min_dist = float('inf')
        for i in range(1, len(mylist)):
            diff = mylist[i] - mylist[i - 1]
            if diff < min_dist:
                min_dist = diff

        max_dist = mylist[-1] - mylist[0]

        return [min_dist, max_dist]
