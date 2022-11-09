# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/



class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        N = len(chalk)
        
        if k % total == 0:
            return 0
        
        left = k % total
        for i in range(N):
            left -= chalk[i]
            if left < 0 :
                return i
