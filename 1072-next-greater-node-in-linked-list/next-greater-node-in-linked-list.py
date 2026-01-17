# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nextLargerNodes(self, head):
        values = []
        
        # Step 1: Convert linked list to array
        while head:
            values.append(head.val)
            head = head.next
        
        res = [0] * len(values)
        stack = []   # stack stores indices
        
        # Step 2: Monotonic stack
        for i in range(len(values)):
            while stack and values[i] > values[stack[-1]]:
                idx = stack.pop()
                res[idx] = values[i]
            stack.append(i)
        
        return res
