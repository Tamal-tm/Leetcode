# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        first = head
        for _ in range(k - 1):
            first = first.next

        kth_from_start = first

        second = head
        while first.next:
            first = first.next
            second = second.next

        kth_from_end = second

        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

        return head
