class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_arr = [(p,s) for p, s in zip(position, speed)]
        car_arr = sorted(car_arr, reverse = True)
        stack = []
        for p, s in car_arr:
            time_taken = (target - p)/s
            stack.append(time_taken)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

