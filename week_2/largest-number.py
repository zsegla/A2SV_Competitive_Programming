# https://leetcode.com/problems/largest-number/



class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
            
        def compare(x,y):
            if x+y > y+x:
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(compare))
        
        return str(int("".join(nums)))
        
        
