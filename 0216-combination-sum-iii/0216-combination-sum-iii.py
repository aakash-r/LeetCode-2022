class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l = 0
        i = 0
        res = []
        com = list(range(1,10))
        cur = []
        def comsum(i,cur,total,l):
            if total==n and l==k:
                res.append(cur.copy())
                return
            if total>n or l>k or i>8:
                return
            
            
            
            comsum(i+1,cur,total,l)
            cur.append(com[i])
            comsum(i+1, cur, total+com[i],l+1)
            cur.pop()
        comsum(0,cur,0,l)
        return res
            
            
            
            
        