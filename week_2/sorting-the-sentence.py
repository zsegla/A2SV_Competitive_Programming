# https://leetcode.com/problems/sorting-the-sentence/



class Solution:
    def sortSentence(self, s: str) -> str:
       
        shuffle = s.split(" ")
        sorted_sentence = ""
        
        for i in range ( len(shuffle)):
            min_idx = i
            for j in range(i+1, len(shuffle)):
                if shuffle[j][-1] < shuffle[min_idx][-1]:
                    min_idx = j
            if i != min_idx:
                shuffle[min_idx], shuffle[i] = shuffle[i], shuffle[min_idx]
            sorted_sentence += shuffle[i][:-1] + ' '
        
        return (sorted_sentence[:-1])
