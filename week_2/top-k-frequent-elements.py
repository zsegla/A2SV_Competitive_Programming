# https://leetcode.com/problems/top-k-frequent-elements/submissions/



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        return (sorted(dic.keys(), key=dic.get, reverse=True)[:k])
