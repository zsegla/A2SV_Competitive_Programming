# https://leetcode.com/problems/find-all-anagrams-in-a-string/



class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        freq = defaultdict(int)
        result = []
        
        if n > len(s):
            return result
        
        def update_freq(c, step):
            freq[c] += step
            if freq[c] == 0:
                del freq[c]
                
        for c1,c2 in zip(p, s[:n]):
            update_freq(c1, -1)
            update_freq(c2, 1)
            
        for i in range(len(s) - n):
            if not freq:
                result.append(i)
            update_freq(s[i], -1)
            update_freq(s[i + n], 1)   
            
        if not freq:
            result.append(len(s) - n)
        
        return result
