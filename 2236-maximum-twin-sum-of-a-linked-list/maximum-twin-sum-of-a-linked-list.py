# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        max_value=0
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        
        prev=None
        curr=slow
        front=slow
        
        while curr is not None:
            front=front.next
            curr.next=prev
            prev=curr
            curr=front
        
        lag=head
        lead=prev
        
        while lead is not None:
            value=lead.val+lag.val
            if max_value < value:
                max_value=value
            lead=lead.next
            lag=lag.next

        return max_value
        
        