# https://leetcode.com/problems/kth-largest-element-in-a-stream/



class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        if len(self.nums) == self.k and val <= self.nums[0]:
            return self.nums[0]
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
            
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
