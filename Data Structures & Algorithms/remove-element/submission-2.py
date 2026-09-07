class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack = []
        for num in nums:
            if num == val:
                continue
            stack.append(num)
        for i in range(len(stack)):
            nums[i] = stack[i]
        return len(stack)