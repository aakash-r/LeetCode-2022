class Solution:
    def ones(self, n):
        ans = 0
        while n>0:
            if n%2!=0:
                ans+=1
            n=n//2
        return ans
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i in arr:
            dic[self.ones(i)].append(i)
        #print(dic)
        ans = []
        for j,i in sorted(dic.items()):
            ans += sorted(i)
        return ans
        
        