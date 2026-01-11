# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Step 1: count total nodes
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        
        # If head needs to be removed
        if length == n:
            return head.next
        
        # Step 2: reach node just before target
        temp = head
        for _ in range(length - n - 1):
            temp = temp.next
        
        # Step 3: remove node
        temp.next = temp.next.next
        
        return head
