class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        a = 0
        for i in range(len(time)):
            time[i] = time[i]%60
        
        dic = {}
        
        for i in time:
            req = 60 - i
            if dic.get(req,-1)!=-1:
                a+=dic[req]
            dic[i] = dic.get(i,0)+1
        #print(dic)
        if dic.get(0,-1)!=-1:
            a+= int((dic[0]*(dic[0]-1))/2)
        return a
    
        