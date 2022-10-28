# https://leetcode.com/problems/fruit-into-baskets/



class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        prev = [None, float("inf"), float("inf")]
        other = [None, float("inf"), float("inf")]
        
        result = 1
        
        for i, fruit in enumerate(fruits):
            if fruit == prev[0]:
                prev[2] = i
                result = max(result, i + 1 - min(prev[1], other[1]))
                
            elif fruit == other[0]:
                other[2] = i
                other, prev = prev,other
                result = max(result, i + 1 - min(prev[1], other[1]))
                
            elif prev[0] is None:
                prev = [fruit, i, i]
                
            elif other[0] is None:
                other, prev = prev, [fruit, i, i]
                result = max(result, i+1-other[1])
                
            else:
                other = [prev[0], other[2]+1, prev[2]]
                prev = [fruit, i, i]
                
        return result
