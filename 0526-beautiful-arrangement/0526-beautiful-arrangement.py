class Solution:
    def countArrangement(self, n: int) -> int:
        rem = list(range(1,n+1))
        res = []
        r = rem.copy()
        
        def search(cur,rem,ind):
            if len(rem)==0:
                res.append(cur.copy())
            
            for i in range(len(rem)):

                num = rem[i]
                if num%ind==0 or ind%num==0:
                    cur.append(num)
                    
                    search(cur.copy(),rem[:i]+rem[i+1:], ind+1)
                    cur.pop()
                elif num%ind!=0 and ind%num!=0:
                    continue
        search([],r,1)
        
        return len(res)