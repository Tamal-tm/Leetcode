# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        slow = head
        fast = head.next

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        while fast:
            gcd_val = gcd(slow.val, fast.val)
            new_node = ListNode(gcd_val)

            slow.next = new_node
            new_node.next = fast

            slow = fast
            fast = fast.next

        return head
