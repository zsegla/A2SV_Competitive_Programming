# https://leetcode.com/problems/xor-queries-of-a-subarray/



class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        for num in arr:
            xor.append(xor[-1] ^ num)
        result = []
        for start, end in queries:
            result.append(xor[end + 1] ^ xor[start])
            
        return result
