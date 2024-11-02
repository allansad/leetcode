class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if current_profit < 0:
                left = right
            else:
                max_profit = max(current_profit, max_profit)
            right += 1 
        return max_profit
            