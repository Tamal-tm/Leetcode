# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        # Step 1: Reverse the linked list
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        head = reverse(head)
        
        # Step 2: Remove nodes smaller than max so far
        max_val = 0
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        
        # Step 3: Reverse again to restore order
        return reverse(dummy.next)