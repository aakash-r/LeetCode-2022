class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0 
        i = 0
        cur = []
        res = []
        
        def comsum(i,total,cur):
            if total == target:
                res.append(cur.copy())
                return
        
            if total>target or i>=len(candidates):
                return 
            
            
            comsum(i+1,total,cur)
            cur.append(candidates[i])
            comsum(i,total + candidates[i], cur)
            cur.pop()
           
        comsum(0,0,[])
        return res