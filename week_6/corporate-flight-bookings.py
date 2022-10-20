# https://leetcode.com/problems/corporate-flight-bookings/



class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n + 1)
        
        for start, end, seats in bookings:
            result[start - 1] += seats
            result[end] -= seats
            
        seats = 0
        for i, change in enumerate(result):
            seats += change
            result[i] = seats
            
        return result[:-1]
