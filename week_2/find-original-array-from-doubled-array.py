# https://leetcode.com/problems/find-original-array-from-doubled-array/



class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        size = len(changed) 
        if size % 2 != 0:
            original = []
        temp = Counter(changed)
        result = []
        for i in sorted(changed, key = lambda x: abs(x)):
            if temp[i] == 0:
                continue
            if temp[2*i] == 0:
                return []
            result += [i]
            if i == 0 and temp[i] <= 1: 
                return []
            temp[i] -= 1
            temp[2*i] -= 1
        
        return result
