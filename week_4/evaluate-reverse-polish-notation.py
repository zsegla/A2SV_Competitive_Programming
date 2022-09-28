# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "/", "*"}
        
        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()
                if token == "/":
                    stack.append(int(left/float(right)))
                else:
                    stack.append(eval(str(left) + token + str(right)))
            else:
                stack.append(int(token))
                
        return stack[-1]
