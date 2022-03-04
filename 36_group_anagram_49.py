class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapResult = {}
        
        def getHash(s:str):
            return "".join(sorted(s))
        
        for s1 in strs:
            key = getHash(s1)
            
            
            if key in mapResult:
                mapResult[key].append(s1)
            else:
                mapResult[key] = [s1]
        
        
        return mapResult.values()
        