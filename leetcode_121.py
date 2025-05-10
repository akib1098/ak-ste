class Solution:
    def maxProfit(self, prices):
        k = 0
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                k+=1
        if k == len(prices):
            return 0
        minimum = min(prices)
        short_list = prices[prices.index(minimum):]
        maximum = max(short_list)
        prof = maximum - minimum
        return prof
s = Solution()
pricess = [7,1,5,3,6,4]
print(s.maxProfit(pricess))
