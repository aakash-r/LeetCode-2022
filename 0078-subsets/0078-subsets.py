class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i=0
        cur = []
    
        
        def dfs(i,cur):
            if i==len(nums):
                res.append(cur.copy())
                return 
            
            dfs(i+1,cur.copy())
            cur.append(nums[i])
            dfs(i+1,cur.copy())
            #cur.pop()
        dfs(0,[])
        return res
                
            