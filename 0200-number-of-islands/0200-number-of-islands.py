class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def rec(i,j):
            if grid[i][j] == '0':
                dic[(i,j)]=1
                return
            elif grid[i][j] == '1':
                dic[(i,j)]=1
            
                
                if i+1<lg and dic.get((i+1,j),0)==0 and grid[i+1][j]=='1':
                    rec(i+1,j)
                    
                if j+1<lr and dic.get((i,j+1),0)==0 and grid[i][j+1]=='1':
                    rec(i,j+1)
                    
                if i-1>=0 and dic.get((i-1,j),0)==0 and grid[i-1][j]=='1':
                    rec(i-1,j)
                    
                if j-1>=0 and dic.get((i,j-1),0)==0 and grid[i][j-1]=='1':
                    rec(i,j-1)
                 
        lg = len(grid)
        lr = len(grid[0])
        
        dic = {}        
        ans = 0
        for i in range(lg):
            for j in range(lr):
                if grid[i][j]=='1' and dic.get((i,j),0)==0:
                    rec(i,j)
                    
                    ans+=1
                elif grid[i][j]=='0' and dic.get((i,j),0)==0:
                    dic[(i,j)]=1
        
        return ans
                
                    
        