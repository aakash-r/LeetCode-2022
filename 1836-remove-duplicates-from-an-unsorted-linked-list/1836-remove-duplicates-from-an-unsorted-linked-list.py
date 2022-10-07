# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dic = {}
        node = head
        prev = ListNode(-1,head)
        root = prev
        while node:
            dic[node.val] = dic.get(node.val,0)+1
            node = node.next
        #print(dic)
        cur = head
        while cur:
            if dic[cur.val] >1:
                prev.next = cur.next
                cur = cur.next
                
            else:
                prev= prev.next
                cur = cur.next
        return root.next
            
        