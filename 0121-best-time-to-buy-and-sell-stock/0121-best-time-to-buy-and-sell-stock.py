class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        msofar = prices[0]
        mpro = 0
        for i in prices[1:]:
            if i > msofar:
                mpro = max(mpro, i-msofar)
            else:
                msofar = i
        return mpro
            
        
            
        
        