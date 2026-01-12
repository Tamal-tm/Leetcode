# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        maxSum = 0
        while head:
            maxSum = max(maxSum, prev.val + head.val)
            prev = prev.next
            head = head.next

        return maxSum


        