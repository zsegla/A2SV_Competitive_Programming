# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/



class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        
        l,r=0, len(nums)-1
        while len(result) != len(nums):
            result.append(nums[l])
            l += 1
            
            if l <= r:
                result.append(nums[r])
                r -= 1
                
        return result
