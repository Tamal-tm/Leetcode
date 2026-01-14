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
    def splitListToParts(self, head, k):
        # 1️⃣ Count total length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # 2️⃣ Calculate base size and extra nodes
        part_size = length // k
        extra = length % k

        result = []
        curr = head

        # 3️⃣ Split into k parts
        for _ in range(k):
            part_head = curr
            size = part_size + (1 if extra > 0 else 0)

            if extra > 0:
                extra -= 1

            # Move to the end of this part
            for i in range(size - 1):
                if curr:
                    curr = curr.next

            # Cut the list
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            result.append(part_head)

        return result
