class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        neg_stones = [-s for s in stones]
        
        while len(neg_stones) > 1:
            print(neg_stones)
            heapq.heapify(neg_stones)
            first = -1*heapq.heappop(neg_stones)
            second = -1*heapq.heappop(neg_stones)
            if first == second:
                continue
            else:
                diff = second - first
                heapq.heappush(neg_stones, diff)
        return -1*heapq.heappop(neg_stones) if neg_stones else 0