class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wl = len(word)
        
        
        def dfs(curpos, wi):
            #print(type(prev))
            if wi == wl:
                return True
            if curpos[0]>=m or curpos[1]>=n or curpos[0]<0 or curpos[1]<0 or board[curpos[0]][curpos[1]] != word[wi]:
                return
            
           
                    
            possible = [(curpos[0]+1,curpos[1]),(curpos[0]-1,curpos[1]),(curpos[0],curpos[1]+1),(curpos[0],curpos[1]-1)]
            temp = board[curpos[0]][curpos[1]]
            board[curpos[0]][curpos[1]] = ","
            for newpos in possible:
                if dfs(newpos,wi+1):
                    return True
            board[curpos[0]][curpos[1]] = temp
                            
        if wl>m*n: return False
        wdic = {}
        boarddic = {}
        for i in range(m):
            for j in range(n):
                boarddic[board[i][j]] = boarddic.get(board[i][j],0)+1
        for l in word:
            wdic[l]=wdic.get(l,0)+1
        
        for i,j in wdic.items():
            if boarddic.get(i,-1) == -1:
                return False
            if boarddic[i]<j:
                return False
        
        
        for i in range(m):
            for j in range(n):
                if dfs((i,j),0):
                    return True
                    
        return False
                
            
        