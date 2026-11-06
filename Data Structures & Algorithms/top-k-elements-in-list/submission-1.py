class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order_dict = {}
        for num in nums:
            order_dict[num] = order_dict.get(num,0) + 1
        sorted_nums = sorted(order_dict.keys(), key=lambda num: order_dict[num], reverse=True)
        return sorted_nums[:k]