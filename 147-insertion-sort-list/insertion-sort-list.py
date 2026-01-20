# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        dummy = ListNode(val=-5001, next=head)
        prev, cur = head, head.next
        while cur:
            if cur.val>=prev.val:
                prev = prev.next
            else:
                tmp = dummy
                while tmp.next.val<=cur.val:
                    tmp = tmp.next
                prev.next = cur.next
                cur.next = tmp.next
                tmp.next = cur
            cur = prev.next

        return dummy.next


        