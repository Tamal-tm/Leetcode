# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        temp=head
        if temp.next is None:
            return head

        def get_gcd(x,y):
            if x>y:
                return get_gcd(y,x)
            else:
                for i in range(1,x+1):
                    if x % i == 0 and y % i == 0:
                        store=i
                return store


        while temp.next is not None:
            next_val=temp.next
            cd=get_gcd(temp.val,next_val.val)
            x=ListNode(cd)
            temp.next=x
            x.next=next_val
            temp=next_val
        
        return head
        