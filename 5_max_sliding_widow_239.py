class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        q = collections.deque()
        result = []
        
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r-l +1 ==k):
                result.append(nums[q[0]])
                l = l + 1
            
            r = r + 1
        
        return result