class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        l = 0
        winS = {}
        winT = {}
        
        for t1 in t:
            winT[t1] = winT.get(t1,0) + 1
            
        have = 0
        want = len(winT)
        res = [-1,-1]
        resLen = float("infinity")
        
        for r in range( len(s) ):
            c = s[r]
        
            winS[c] = winS.get(c,0) + 1
                
            if c in t and winS[c] == winT[c]:
                have = have + 1
            
            while have == want:
                length = r-l + 1
                
                if length < resLen:
                    resLen = length
                    res = [l,r]
                
                # make it smaller
                
                winS[s[l]] = winS[s[l]]-1
                
                if s[l] in t and winS[s[l]] < winT[s[l]]:
                    have = have - 1
                
                l = l+1
        
        l,r = res
        
        return s[l:r+1] if resLen != float("infinity") else ""