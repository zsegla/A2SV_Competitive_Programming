# https://leetcode.com/problems/palindrome-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        rev = None
        
        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = rev 
            rev = slow
            slow = next_slow
            
        if fast:
            slow = slow.next
            
        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
            
        return True
