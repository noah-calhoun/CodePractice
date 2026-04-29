# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List


def maxProfitOld(prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1 
        while l <= len(prices) - 1:
            if r < len(prices) and (prices[r] > prices[l]):
                profit = max(prices[r] - prices[l], profit)
                r += 1
            else:
                l, r = l + 1, l + 2
        return profit

def maxProfit(prices: List[int]) -> int:
    profit = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = max(profit, prices[r] - prices[l])
        else:
            l = r
        r += 1

    return profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices=[5,1,5,6,7,1,10]
    print(maxProfit(prices))
