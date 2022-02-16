class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)> len(s):
            return []
        
        ps, pp = {}, {}
        
        for i in range( len(p)):
            ps[s[i]] = 1 + ps.get(s[i], 0)
            pp[p[i]] = 1 + pp.get(p[i], 0)
            
        result = [0] if ps == pp else []
        
        l = 0
        
        for r in range(len(p), len(s)):
            ps[s[r]] = ps.get(s[r], 0) + 1
            ps[s[l]] = ps[s[l]] -1
            
            if ps[s[l]] == 0 :
                ps.pop(s[l])
            
        
            l = l+1
            
            if ps == pp:
                result.append(l)
    
        return result