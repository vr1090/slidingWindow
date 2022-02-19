"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMax, curMin = 1,1
        
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1,1
                continue
            
            tmpMax = curMax
            curMax = max( n* curMax, n*curMin, n)
            curMin = min(n*tmpMax, n*curMin, n)
            result = max(curMax, curMin, result)
            
        return result