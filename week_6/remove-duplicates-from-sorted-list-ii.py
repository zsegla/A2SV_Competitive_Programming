# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pseudo = prev = ListNode(None)
        pseudo.next = head
        node = head
        
        while node:
            if node.next and node.val == node.next.val:
                duplicate_val = node.val
                node = node.next
                while node and node.val == duplicate_val:
                    node = node.next
                prev.next = None
            else:
                prev.next = node
                prev = node
                node = node.next
        return pseudo.next
