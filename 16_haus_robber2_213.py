class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def hausRob(anums:List[int])-> int :
            rob1, rob2 = 0,0
            
            for n in anums:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        
        return max(nums[0], hausRob(nums[:-1]), hausRob(nums[1:]))