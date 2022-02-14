class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        
        i =0
        j = i+1
        
        while j < len(prices) :
            if prices[i] < prices[j]:
                maxPrice = max(maxPrice, prices[j]- prices[i])
            else:
                i = j 
            
            j = j + 1 
        
        return maxPrice