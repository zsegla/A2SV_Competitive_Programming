# https://leetcode.com/problems/find-target-indices-after-sorting-array/



class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if target == nums[i]:
                ans.append(i)
        return ans
        
