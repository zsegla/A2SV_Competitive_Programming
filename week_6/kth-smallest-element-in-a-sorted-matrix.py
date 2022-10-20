# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/



class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        if k > (rows * cols)//2:
            back = True
            k = rows * cols - k + 1
            frontier = [(-matrix[rows - 1][cols - 1], rows - 1, cols - 1)]
        else:
            back = False
            frontier = [(matrix[0][0], 0, 0)]
            
        while k :
            val, r, c = heapq.heappop(frontier)
            k -= 1
            if not back:
                if c != len(matrix[0]) - 1:
                    heapq.heappush(frontier, (matrix[r][c+1], r, c + 1))
                if c == 0 and r != len(matrix) - 1:
                    heapq.heappush(frontier, (matrix[r+1][c], r + 1, c))        
            else:
                if c != 0:
                    heapq.heappush(frontier, (-matrix[r][c-1], r, c-1))
                    if c == cols - 1 and r != 0:
                        heapq.heappush(frontier, (-matrix[r-1][c], r-1, c))
                        
        return -val if back else val
