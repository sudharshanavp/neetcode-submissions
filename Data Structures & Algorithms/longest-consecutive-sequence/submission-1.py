class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seq_map = {}

        if not nums:
            return 0

        for num in nums:
            seq_map[num] = 1

        for num in nums:
            next_num = num
            isSequence = True
            while isSequence:
                next_num+=1
                if next_num in seq_map and seq_map[next_num] != -1:
                    seq_map[num] += seq_map[next_num]
                    seq_map[next_num] = -1
                else:
                    isSequence = False                

        res = max(seq_map, key = lambda x: seq_map.get(x))
        return seq_map[res]