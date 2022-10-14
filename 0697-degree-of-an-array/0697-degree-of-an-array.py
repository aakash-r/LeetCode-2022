class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        data = list(dic.items())
        d = defaultdict(list)
        for i,j in data:
            d[j].append(i)
        maxc = max(d.keys())
        possible = d[maxc]
        ans = []
        
        for cur in possible:
            start = 0
            end = len(nums)-1
            while start<len(nums) and nums[start]!=cur:
                start+=1

            while end>0 and nums[end]!=cur:
                end-=1

            l = end-start+1
            ans.append(l)
        return min(ans)
        
        
        
        
        
        