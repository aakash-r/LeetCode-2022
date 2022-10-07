class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for i in items:
            dic[i[0]].append(i[1])
            
        #print(dic)
        ans = []
        for i,j in sorted(dic.items()):
            avg = sum(sorted(j)[::-1][:5])//5
            ans.append([i,avg])
            
        return ans
        