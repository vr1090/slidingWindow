class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =0
        charCount = {}
        result = 0
        
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            
            while (r-l+1) - max(charCount.values()) > k :
                charCount[s[l]] = charCount[s[l]]- 1
                l = l + 1
            
            result = max( result, r-l + 1)
            
        
        return result# window len, that we need to replace
