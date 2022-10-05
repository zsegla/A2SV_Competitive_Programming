# https://leetcode.com/problems/reverse-nodes-in-k-group/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head
        
        node = head
        for i in range(k):
            if not node:
                return head
            node = node.next
            
        prev = self.reverseKGroup(node, k)
        
        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            
        return prev
