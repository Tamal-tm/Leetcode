# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        slow = head
        fast = head.next

        while fast:
            a = slow.val
            b = fast.val
            while b:
                a, b = b, a % b

            slow.next = ListNode(a, fast)
            slow = fast
            fast = fast.next

        return head
