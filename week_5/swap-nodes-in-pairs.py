# https://leetcode.com/problems/swap-nodes-in-pairs/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(None)
        
        while head and head.next:
            next_head = head.next.next
            prev.next = head.next
            head.next.next = head
            prev = head
            head = next_head
            
        prev.next = head
        return dummy.next
