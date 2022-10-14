class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        counts = {}
        for i,ind in enumerate(nums):
            if len(d[ind])>1:
                d[ind].pop()
            d[ind].append(i)
            counts[ind]=counts.get(ind,0)+1
        maxc = max(counts.values())
        minl = len(nums)
        if maxc == 1:
            return 1
        for i,j in counts.items():
            if j==maxc:
                minl=min(minl, d[i][1]-d[i][0]+1)
        return minl
        
        
        
        
        
        
        
        