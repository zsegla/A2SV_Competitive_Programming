# https://leetcode.com/problems/next-greater-node-in-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []
        stack = []
        node = head
        i = 0
        
        while node:
            result.append(0)
            while stack and stack[-1][1] < node.val:
                j, _ = stack.pop()
                result[j] = node.val
                
            stack.append((i, node.val))
            i += 1
            node = node.next
            
        return result
