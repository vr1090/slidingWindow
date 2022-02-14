class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        setChar = set()
        maxLength = 0 
        
        for i in range(len(s)):
            while s[i] in setChar:
                setChar.remove(s[start])
                start = start + 1
            
            
            maxLength = max(maxLength, i - start+1)
            setChar.add(s[i])
            
        
        return maxLength
        
        