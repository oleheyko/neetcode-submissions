class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [p[0]**2 + p[1]**2 for p in points]
        heap = []
        for idx, val in enumerate(distances):
            if idx < k:
                heapq.heappush(heap, (-val, idx))
            else:
                heapq.heappushpop(heap, (-val, idx))
        res = [points[t[1]] for t in heap]
        return res