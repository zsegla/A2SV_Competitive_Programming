# https://leetcode.com/problems/reverse-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        
        while head:
            next = head.next
            head.next = reversed
            reversed = head
            head = next
            
        return reversed
