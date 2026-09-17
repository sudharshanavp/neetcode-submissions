class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i -1])
        return profit
        