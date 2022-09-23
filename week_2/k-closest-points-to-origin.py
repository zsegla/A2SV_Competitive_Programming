# https://leetcode.com/problems/k-closest-points-to-origin/



import math
import collections

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance =[]
        result =[] 
        dictionary=collections.defaultdict(list)
        for p in points:
            d =math.pow(p[0],2) + math.pow(p[1],2)
            dist = math.sqrt(d)
            distance.append(dist)
            dictionary[dist].append(p)
        distance.sort() 
        for i in range(k):
                if len(dictionary [distance [i]])>1:
                    for j in dictionary[distance [i]]:
                       result.append(j)
                    return result
                else:
                    for j in dictionary[distance [i]]:
                          result.append(j)
        
        return result
