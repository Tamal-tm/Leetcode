# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums)
        dummy=ListNode()
        curr=dummy
        temp=head
        
        while temp:
            if temp.val not in nums:
                curr.next = temp
                curr = curr.next
            temp = temp.next
        
        curr.next = None
        return dummy.next

        

        