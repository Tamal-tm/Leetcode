# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        temp=head
        count=1
        while temp is not None:
            if count == k:
                store_val_1=temp.val
            count +=1
            temp=temp.next

        temp=head
        for _ in range(count-k-1):
            temp=temp.next
        store_val_2=temp.val
        temp.val=store_val_1

        temp=head
        count=1
        while temp is not None:
            if k == count:
                temp.val=store_val_2
            count +=1
            temp=temp.next
        
        return head


        
