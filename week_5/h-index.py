# https://leetcode.com/problems/h-index/



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        buckets = [0] * (len(citations)+1)
        
        for cit in citations:
            buckets[min(cit, len(citations))] += 1
            
        papers = 0
        
        for buc in range(len(buckets)-1, -1, -1):
            papers += buckets[buc]
            if papers >= buc:
                return buc
