# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        temp=head
        store=[]
        combined_string=""
        while temp is not None:
            store.append(temp.val)
            temp=temp.next
        combined_string = "".join(map(str, store))

        return int(combined_string,2)