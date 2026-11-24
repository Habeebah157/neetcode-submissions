class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer = 1
        currProf = 0
        lowest = prices[0]
        while pointer < len(prices):
            print("pointer",pointer)
            print("lowest",lowest)
            print("currProf",currProf)
            if prices[pointer] < lowest:
                lowest = prices[pointer]
            elif prices[pointer] > lowest:
                if (currProf) < (prices[pointer] - lowest):
                    currProf = (prices[pointer] - lowest)
            else:
                lowest = lowest
            pointer+=1
        return currProf
        