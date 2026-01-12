# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        temp=head.next
        
        while temp is not None:
            sum_value=0
            initial_head=temp
            while temp.val != 0:
                sum_value +=temp.val
                temp=temp.next
            initial_head.next=temp.next
            initial_head.val=sum_value
            temp = initial_head.next

        return head.next