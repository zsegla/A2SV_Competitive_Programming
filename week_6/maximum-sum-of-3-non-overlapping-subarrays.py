# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/




class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        one_sum = sum(nums[:k])
        two_sum = sum(nums[k: k *2])
        three_sum = sum(nums[k*2:k*3])
        
        best_one = one_sum
        best_two = one_sum + two_sum
        best_three = one_sum + two_sum + three_sum
        
        best_one_i = 0
        best_two_i = [0, k]
        best_three_i = [0, k, k*2]
        
        one_i = 1
        two_i = k + 1
        three_i = k * 2 + 1
        
        while three_i <= len(nums) - k:
            one_sum += nums[one_i + k - 1] - nums[one_i - 1]
            two_sum += nums[two_i + k - 1] - nums[two_i -1]
            three_sum += nums[three_i + k -1] - nums[three_i -1]
            
            if one_sum > best_one:
                best_one = one_sum
                best_one_i = one_i
                
            if best_one + two_sum > best_two:
                best_two = best_one + two_sum
                best_two_i = [best_one_i, two_i]
                
            if best_two + three_sum > best_three:
                best_three = best_two + three_sum
                best_three_i = best_two_i + [three_i]
                
            one_i += 1
            two_i += 1
            three_i += 1
            
        return best_three_i
