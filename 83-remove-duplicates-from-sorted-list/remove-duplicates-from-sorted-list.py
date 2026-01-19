# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy=ListNode()
        curr=dummy
        temp=head
        mylist=[]

        while temp is not None:
            if temp.val not in mylist:
                mylist.append(temp.val)
            temp=temp.next
        
        for i in range(len(mylist)):
            curr.next=ListNode(mylist[i])
            curr=curr.next
        
        return dummy.next

        