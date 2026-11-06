class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]*len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_index, prev_temp = stack.pop()
                days[prev_index] = index - prev_index
            # Today joins the waiting room for its own future warmer day
            stack.append((index, temp))
        return days
                
