# https://leetcode.com/problems/daily-temperatures/



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackT, prev_i = stack.pop()
                result[prev_i] = i - prev_i
                
            stack.append((temp, i))
        
        return result
