# https://leetcode.com/problems/validate-stack-sequences/



class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
                
        return i == len(popped)
