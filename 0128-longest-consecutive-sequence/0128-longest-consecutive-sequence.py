class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)

        maxl = 0
        
        for n in nums:
            templ = 0
            temp = n
            if n-1 in data:
                continue
            else:
                while temp in data:
                    templ+=1
                    temp+=1
                maxl = max(templ,maxl)
        return maxl
            
            
        