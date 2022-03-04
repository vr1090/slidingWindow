class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        mapC = {}
        l = 0
        
        for r in range( len(s)):
            mapC[s[r]] = mapC.get(s[r], 0) + 1
            
            while (r-l+1)- max(mapC.values()) > k:
                mapC[s[l]] = mapC[s[l]] - 1
                l = l+1
            
            result = max( result, r-l+1)
        
        return result