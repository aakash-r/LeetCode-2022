# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#TWO PASSSSSSSS
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first=head
        second=head
        i=0
        while i<n+1:
            try:
                first=first.next
            except:
                return head.next
            i+=1
        #print(first.val)
        while first is not None:
            second=second.next
            first=first.next
        
        #print(second.val)
        second.next=second.next.next
        return head