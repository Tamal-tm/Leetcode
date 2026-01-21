# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseEvenLengthGroups(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        group_size = 1

        while curr:
            # Step 1: count actual nodes in this group
            count = 0
            temp = curr
            while temp and count < group_size:
                temp = temp.next
                count += 1

            # Step 2: if count is even → reverse
            if count % 2 == 0:
                prev_next = curr
                prev_rev = None

                for _ in range(count):
                    nxt = curr.next
                    curr.next = prev_rev
                    prev_rev = curr
                    curr = nxt

                prev.next = prev_rev
                prev_next.next = curr
                prev = prev_next

            else:
                # Step 3: if odd → just move pointers
                for _ in range(count):
                    prev = curr
                    curr = curr.next

            group_size += 1

        return dummy.next
