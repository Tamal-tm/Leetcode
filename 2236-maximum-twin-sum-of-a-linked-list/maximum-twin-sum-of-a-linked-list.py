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
    def pairSum(self, head):
        f = head
        node = None
        maxSum = 0
        while f:
            f = f.next.next
            temp = head.next
            head.next = node
            node = head
            head = temp
        while head:
            maxSum = max(maxSum,node.val + head.val)
            node = node.next
            head = head.next
        return maxSum
        """
        :type head: Optional[ListNode]
        :rtype: int
        """