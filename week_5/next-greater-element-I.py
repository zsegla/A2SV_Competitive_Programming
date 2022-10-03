# https://leetcode.com/problems/next-greater-element-i/



class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        find_to_i = {}
        
        for i, num in enumerate(nums1):
            find_to_i[num] = i
            
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                if smaller in find_to_i:
                    result[find_to_i[smaller]] = num
            stack.append(num)
            
        return result
