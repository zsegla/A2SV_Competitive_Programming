# https://leetcode.com/problems/max-number-of-k-sum-pairs/



class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        dic = {}
        
        for num in nums:
            t = k - num
            if t in dic and dic[t]>0:
                result += 1
                dic[t] -= 1
            else:
                if num not in dic:
                    dic[num] = 0 
                dic[num] += 1
            
        return result
