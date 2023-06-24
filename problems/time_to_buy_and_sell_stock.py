"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_price = prices[0] # first day price

        for sell_price in prices[1:]:
            current_profit = sell_price - buy_price
            if current_profit > max_profit:
                max_profit = current_profit
            elif sell_price < buy_price:
                buy_price = sell_price

        return max_profit

# test cases
solution = Solution()
result = solution.maxProfit([2,4,1])
print(result)

result = solution.maxProfit([7,1,5,3,6,4])
print(result)