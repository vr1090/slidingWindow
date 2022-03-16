class TreeNode:
    def __init__(self):
        self.child = {}
        self.word = False

class WordDictionary:

            
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.child:
                cur.child[c] =TreeNode()
            cur = cur.child[c]
        
        cur.word = True
        
        
        

    def search(self, word: str) -> bool:
    
        def dfs(pos, node):
            cur = node
             
            
            for i in range(pos, len(word)):
                ch = word[i]
                if ch ==".":
                    for nd in cur.child.values():
                        if dfs(i+1, nd):
                            return True
                    return False
                else:
                    if ch not in cur.child:
                        return False
                    cur = cur.child[ch]
            return cur.word
        
        return dfs(0,self.root)