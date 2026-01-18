# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        temp=head
        values=[]
        count=0
        
        while temp is not None:
            values.append(temp.val)
            count+=1
            temp=temp.next
        single_integer = int("".join(map(str, values)))
        main_val=2*single_integer
        back_to_list = list(map(int, str(main_val)))
        check=len(back_to_list)
        temp=head
        i=0
        while temp is not None:
            temp.val=back_to_list[i]
            if i == count-1:
                break
            temp=temp.next
            i+=1

        new_node=ListNode(back_to_list[-1])
        if check !=count:
            temp.next=new_node
            
        return head
