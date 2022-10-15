class Solution:
    res = 0
    def countArrangement(self, n: int) -> int:
        rem = list(range(1,n+1))
        r = rem.copy()
        self.search([],r,1)
        return self.res
        
        
        
    def search(self,cur,rem,ind):
        if len(rem)==0:
            self.res+=1
            
        for i in range(len(rem)):

            num = rem[i]
            if num%ind==0 or ind%num==0:
                cur.append(num)
                    
                self.search(cur.copy(),rem[:i]+rem[i+1:], ind+1)
                cur.pop()
            elif num%ind!=0 and ind%num!=0:
                continue
        