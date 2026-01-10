# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        temp=head
        mydict={}
        
        while temp is not None:
            if temp in mydict:
                return temp
            mydict[temp]=True
            temp=temp.next
        
        return None
        