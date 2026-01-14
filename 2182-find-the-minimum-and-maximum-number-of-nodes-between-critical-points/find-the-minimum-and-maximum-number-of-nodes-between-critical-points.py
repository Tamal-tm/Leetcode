# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        mylist = []

        prev = head
        curr = head.next
        pos = 2

        if not curr or not curr.next:
            return [-1, -1]

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                mylist.append(pos)

            prev = curr
            curr = curr.next
            pos += 1

        if len(mylist) < 2:
            return [-1, -1]

        min_dist = float('inf')
        for i in range(1, len(mylist)):
            min_dist = min(min_dist, mylist[i] - mylist[i-1])

        max_dist = mylist[-1] - mylist[0]

        return [min_dist, max_dist]
