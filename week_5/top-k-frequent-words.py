# https://leetcode.com/problems/top-k-frequent-words/



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        pairs = [(-count, word) for word, count in freq.items()]
        heapq.heapify(pairs)
        
        return [heapq.heappop(pairs)[1] for _ in range(k)]
