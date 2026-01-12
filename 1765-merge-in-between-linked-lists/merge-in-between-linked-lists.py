# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        curr = list1

        for _ in range(a - 1):
            curr = curr.next

        prevA = curr

        for _ in range(b - a + 2):
            curr = curr.next

        afterB = curr

        prevA.next = list2

        tail = list2
        while tail.next:
            tail = tail.next

        tail.next = afterB

        return list1
