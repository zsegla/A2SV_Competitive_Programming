# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/



class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)
        dic = {}
        result = []
        
        for i in range( len(sorted_arr)):
            if sorted_arr[i] not in dic:
                dic[sorted_arr[i]] = i
        
        for i in nums:
            result.append(dic[i])
        return result
