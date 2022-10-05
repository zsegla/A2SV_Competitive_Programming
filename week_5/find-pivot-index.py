# https://leetcode.com/problems/find-pivot-index/



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        
        for i, num in enumerate(nums):
            right -= num
            
            if right == left:
                return i
            
            left += num
            
        return -1
