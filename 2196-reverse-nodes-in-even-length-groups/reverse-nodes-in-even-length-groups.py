class Solution(object):
    def reverseEvenLengthGroups(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        size = 1

        while curr:
            cnt = 0
            node = curr
            while node and cnt < size:
                node = node.next
                cnt += 1

            if cnt & 1 == 0:
                last = curr
                prev_rev = None
                for _ in range(cnt):
                    nxt = curr.next
                    curr.next = prev_rev
                    prev_rev = curr
                    curr = nxt
                prev.next = prev_rev
                last.next = curr
                prev = last
            else:
                for _ in range(cnt):
                    prev = curr
                    curr = curr.next

            size += 1

        return dummy.next
