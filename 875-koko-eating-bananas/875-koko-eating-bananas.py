class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = ceil(sum(piles)/h)
        r = max(piles)
        #print(l,r)
        while l<r:
            hrem = h
            mid = (l+r)//2
            for i in piles:
                if i<=mid:
                    hrem-=1
                else:
                    hrem-= ceil(i/mid)
            if hrem>=0:
                r = mid
            else:
                l = mid+1
        return l
                    
            
        