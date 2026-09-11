class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)

        for num in nums:
            count[num]+=1

        for num, frequency in count.items():
            freq[frequency].append(num)
        
        final_arr = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                final_arr.append(num)
                if len(final_arr) == k:
                    return final_arr
        

