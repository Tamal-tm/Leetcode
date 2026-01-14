# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        mylist=[]
        temp=head.next
        prev=head
        count=2
        val=0
        if temp is None:
            return [-1,-1]
        
        if temp.next is None:
            return [-1,-1]

        while temp.next is not None:
            if temp.val > prev.val and temp.val > temp.next.val:
                mylist.append(count)
            if temp.val < prev.val and temp.val < temp.next.val:
                mylist.append(count)
            count +=1
            temp=temp.next
            prev=prev.next
        
        if len(mylist) < 2:
            return [-1, -1]

        min_dist = float('inf')
        for i in range(1, len(mylist)):
            min_dist = min(min_dist, mylist[i] - mylist[i-1])

        max_dist = mylist[-1] - mylist[0]

        return [min_dist, max_dist]