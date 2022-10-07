class Solution: 
    def numTeams(self, rating: List[int]) -> int:
        
        
        ans=0
        for i,j in enumerate(rating):
            ll,lh,rl,rh = 0,0,0,0
            for k in range(0,i):
                if rating[k]>j:
                    lh+=1
                elif rating[k]<j:
                    ll+=1
            for k in range(i+1,len(rating)):
                if rating[k]>j:
                    rh+=1
                elif rating[k]<j:
                    rl+=1
            ans+= (ll*rh) + (lh*rl)
            #print(j,ll,lh,rl,rh)
        return ans
            
            
        