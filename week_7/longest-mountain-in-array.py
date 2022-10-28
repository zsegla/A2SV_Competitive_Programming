# https://leetcode.com/problems/longest-mountain-in-array/



class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        valley, peak = 0, 0
        prev = 0
        longest = 0
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                valley, peak = i, i
                prev = 0
            elif arr[i] > arr[i - 1]:
                if prev == 1:
                    peak = i
                else:
                    valley = i - 1
                prev = 1
            elif arr[i] < arr[i - 1]:
                if prev == 1:
                    peak = i - 1
                    longest = max(longest, i - valley + 1)
                else:
                    if peak > valley:
                        longest = max(longest, i - valley + 1)
                prev = -1
                
        return longest
