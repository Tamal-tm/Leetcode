# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # Remove all matching nodes at the head
        while head and head.val == val:
            head = head.next

        # Now traverse the rest of the list
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head