# https://leetcode.com/problems/boats-to-save-people/



class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0 
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            boats += 1
            if people[light] + people[heavy] <= limit:
                light += 1
                
            heavy -= 1
        return boats
