# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/



class Solution(object):
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        l_sum, m_sum = sum(nums[secondLen:firstLen + secondLen]), sum(nums[firstLen:firstLen+secondLen])
        l_before_m_sum, m_before_l_sum = sum(nums[:firstLen]), sum(nums[:secondLen])
        l_before_m_best, m_before_l_best = l_before_m_sum, m_before_l_sum
        
        result = sum(nums[:firstLen+secondLen])
        
        for i in range(firstLen + secondLen, len(nums)):
            l_sum = l_sum + nums[i] - nums[i - firstLen]
            m_before_l_sum = m_before_l_sum + nums[i - firstLen] - nums[i - firstLen - secondLen]
            m_before_l_best = max(m_before_l_best, m_before_l_sum)
            result = max(result, l_sum + m_before_l_best)
            
            m_sum= m_sum + nums[i] - nums[i - secondLen]
            l_before_m_sum = l_before_m_sum + nums[i - secondLen] - nums[i - firstLen - secondLen]
            l_before_m_best = max(l_before_m_best, l_before_m_sum)
            result = max(result, m_sum + l_before_m_best)
            
        return result
