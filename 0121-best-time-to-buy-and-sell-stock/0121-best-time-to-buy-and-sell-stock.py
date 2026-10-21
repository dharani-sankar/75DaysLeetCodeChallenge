class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minsofar=prices[0]
        profit=0
        for i in range(1,len(prices)):
            minsofar=min(minsofar,prices[i])
            profit=max(profit,prices[i]-minsofar)
        return profit