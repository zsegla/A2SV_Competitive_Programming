# https://leetcode.com/problems/power-of-three/



class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        max_int = 2 ** 31 -1
        max_power = int(math.log(max_int, 3))
        return 3 ** max_power % n == 0
