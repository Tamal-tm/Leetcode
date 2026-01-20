# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(float('-inf'))
        curr = head

        while curr:
            prev = dummy

            # find position to insert current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            next_node = curr.next

            # insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            curr = next_node

        return dummy.next
