# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        fast = head
        for _ in range(k - 1):
            fast = fast.next

        slow = head
        first = fast

        while fast.next:
            fast = fast.next
            slow = slow.next

        first.val, slow.val = slow.val, first.val
        return head
