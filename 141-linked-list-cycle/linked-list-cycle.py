# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        temp=head
        mylist=[]
        
        while temp is not None:
            
            if temp in mylist:
                return True
            mylist.append(temp)
            temp=temp.next
        
        return False
        