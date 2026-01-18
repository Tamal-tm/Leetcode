# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):

        # 1) Reverse the linked list
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        head = prev   # new head after reverse

        # 2) Double each digit with carry
        carry = 0
        cur = head
        last = None

        while cur:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            last = cur
            cur = cur.next

        # 3) If carry remains, add new node
        if carry:
            last.next = ListNode(carry)

        # 4) Reverse again to restore order
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
