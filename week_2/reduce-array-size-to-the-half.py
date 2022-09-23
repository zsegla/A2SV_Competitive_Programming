# https://leetcode.com/problems/reduce-array-size-to-the-half/



class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if not arr:
            return 0

        freqs = collections.Counter(arr)
        target = len(arr) // 2
        curr = 0
        for i, k, in enumerate(sorted(freqs.values(), reverse=True)):
            curr += k
            print(i, k, curr, target)
            if curr >= target:
                return i + 1
        return -1
