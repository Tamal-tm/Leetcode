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
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # 1. Find length and last node
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1

        # 2. Make list circular
        temp.next = head

        # 3. Find new tail
        k = k % length
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # 4. Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head




        