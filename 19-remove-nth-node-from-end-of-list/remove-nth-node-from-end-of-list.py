# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow=head
        fast=head

        for _ in range(n): # Giving headstart by n difference. 
            fast=fast.next

        if fast==None: # End of the list. 
            return head.next
        
        while fast.next: # Will stop at last element
            slow=slow.next
            fast=fast.next
            
        slow.next=slow.next.next
        
        return head




