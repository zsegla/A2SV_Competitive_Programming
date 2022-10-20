# https://leetcode.com/problems/kth-largest-element-in-an-array/



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums)-1
        
        while True:
            index = self.partition(nums,left,right)
            if index == k:
                return nums[index]
            if index > k:
                right = index - 1
            else:
                left = index + 1
                
    def partition(self, nums, left, right):
        rand_index = random.randint(left, right)
        rand_entry = nums[rand_index]
        nums[rand_index], nums[right] = nums[right], nums[rand_index]
        
        next_lower = left
        for i in range(left, right):
            if nums[i] <= rand_entry:
                nums[next_lower], nums[i] = nums[i], nums[next_lower]
                next_lower += 1
        
        nums[next_lower], nums[right] = nums[right], nums[next_lower]
        return next_lower
