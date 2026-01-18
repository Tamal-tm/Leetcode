# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        slow=head
        fast=head
        
        if slow.next is None:
            return None

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        temp=head
        while temp is not None:
            if temp.next==slow:
                temp.next=temp.next.next
            else:
                temp=temp.next
        
        return head