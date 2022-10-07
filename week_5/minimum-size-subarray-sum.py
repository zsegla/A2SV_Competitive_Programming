# https://leetcode.com/problems/minimum-size-subarray-sum/



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub_sum, min_len, start = 0, len(nums) + 1, 0
        
        for i in range(len(nums)):
            sub_sum += nums[i]
            
            while sub_sum >= target:
                min_len = min(min_len, i - start +1)
                sub_sum -= nums[start]
                start += 1
            
        return 0 if min_len > len(nums) else min_len
