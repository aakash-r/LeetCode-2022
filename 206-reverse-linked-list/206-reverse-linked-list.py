class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            cur=head.next
            prev=head
            prev.next=None
            while cur:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            return prev
        else:
            return None