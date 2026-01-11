# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        traverse=0
        count=1
        val=0
        while temp is not None:
            traverse +=1
            temp=temp.next
        
        if n == traverse:
            return head.next
        
        val=traverse-n

        temp=head
        while temp is not None:
            if count == val:
                temp.next=temp.next.next
            count +=1
            temp=temp.next

        return head