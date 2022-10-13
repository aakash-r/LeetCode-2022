class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        rem = nums.copy()
        cur = []
        res = []
        def findperm(cur,rem):
            if len(rem)==0:
                res.append(cur.copy())
                return
            for i in range(len(rem)):
                cur.append(rem[i])
                rem_new = rem[:i]+rem[i+1:]
                findperm(cur,rem_new)
                cur.pop()
                
            
            
        findperm([],rem)
        return res