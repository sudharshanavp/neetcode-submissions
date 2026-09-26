class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store day, temp as list or tuple
        res = [0] * len(temperatures)

        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_day, stack_temp = stack.pop()
                res[stack_day] = day - stack_day
            stack.append((day, temp))
        return res