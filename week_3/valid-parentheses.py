# https://leetcode.com/problems/valid-parentheses/submissions/



class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
        "]" : "[" ,
        "}" : "{" ,
        ")" : "("
    }
        stack = []
        
        for par in s:
            if par in dic:
                if stack and stack[-1] == dic[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        
        return True if not stack else False
    
