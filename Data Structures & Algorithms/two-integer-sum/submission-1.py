class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in seen.values():
                key = next(k for k, v in seen.items() if v == difference)
                return [key, index]
            seen[index] = num
