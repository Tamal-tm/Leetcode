# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if (list1 is None) and (list2 is None):
            return None
        
        newList = ListNode()
        lastNode = newList

        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                nextNode = ListNode(list1.val)
                list1 = list1.next
            else:
                nextNode = ListNode(list2.val)
                list2 = list2.next
            lastNode.next = nextNode
            lastNode = lastNode.next

        if list1 is None:
            lastNode.next = list2
        else:
            lastNode.next = list1

        return newList.next