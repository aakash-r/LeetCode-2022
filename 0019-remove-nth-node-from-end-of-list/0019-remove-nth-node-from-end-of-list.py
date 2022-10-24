# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = head
        
        cur = 0
        l = 0
        while head is not None:
            l+=1
            head=head.next
        d = l-n
        head = root
        while cur<d-1:
            cur+=1
            head=head.next
        if d==0: return root.next
        if head is None: return root
        elif head.next is None: return root
        else:
            temp = head.next.next
            head.next=temp
            return root
            
            
        
        