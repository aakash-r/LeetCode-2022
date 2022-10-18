class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0)+1
        l = len(nums)
        l1 = []
        d = [l1.copy() for i in range(l+1)]
        #print(counts,d)
        
        for i,j in counts.items():
            d[j].append(i)
            #print(d)
        
        ans = []
        p = 0
        #print(d)
        for li in d[::-1]:
            if p<k:
                ans+=li
                p+=len(li)
            else:
                break
        return ans
            
        
        