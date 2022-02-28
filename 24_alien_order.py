class Solution:
    def alienOrder(self, word:List[str])-> str:
        adj = {c:set() for w in word for c in w }

        for i in range( len(words)-1 ):
            w1, w2 = word[i], word[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add( w2[j])
        
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for n in adj[c]:
                if dfs(n):
                    return True
            
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        return "".join(res)

