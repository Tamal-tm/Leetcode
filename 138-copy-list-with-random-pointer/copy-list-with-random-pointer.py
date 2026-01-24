class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # 1️⃣ Insert copied nodes next to originals
        curr = head
        while curr:
            new = Node(curr.val, curr.next)
            curr.next = new
            curr = new.next

        # 2️⃣ Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3️⃣ Separate the two lists
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return copy_head
