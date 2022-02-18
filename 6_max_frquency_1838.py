class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        l = 0
        r = 0
        total = 0
        
        while r < len(nums):
            total += nums[r]
            
            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l = l+ 1
            
            result = max( result, r-l+1)
            r+= 1
        return result