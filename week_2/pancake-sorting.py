# https://leetcode.com/problems/pancake-sorting/



class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        N = len(arr)
        output = []
        
        for i in range (N-1, -1, -1):
            max_ = i
            for j in range (i, -1, -1):
                if  arr[j] > arr[max_]: 
                    max_ = j
                
            if max_ != i:
                flip(max_)
                flip(i)
                output.append(max_+1)
                output.append(i+1)
            
        return output
