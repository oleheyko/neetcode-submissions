class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order_dict = {}
        for num in nums:
            order_dict[num] = order_dict.get(num,0) + 1

        arr = []
        for num, freq in order_dict.items():
            arr.append([freq, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res