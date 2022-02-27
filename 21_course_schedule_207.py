class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            dictDepend = {i:[] for i in range(numCourses)}
            visited = set()
            
            
            for lst in prerequisites:
                dictDepend[lst[0]].append( lst[1])
            
            def dfs(num):
                if num in visited:
                    return False
                
                if dictDepend[num] == [] :
                    return True
                
                visited.add(num)
                
                for n in dictDepend[num]:
                    if not dfs(n): return False
                
                visited.remove(num)
                dictDepend[num] = []
                
                return True
                    
                    
                    
            for n in range(numCourses):
                if not dfs(n):
                    return False
            
            return True

for n in range(last_index):
    for m in range(n+1, last_index+1):
        if data[n] < data[m]:
            data[n], data[m]= data[m], data[n]
                