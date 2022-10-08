class Solution:
    
    
    #better sol
    def countBinarySubstrings(self, s: str) -> int:
        ptr = 0
        s=s+'2'
        groups = []
        count = 1
        while ptr<len(s)-1:
            
            if s[ptr]!=s[ptr+1]:
                groups.append(count)
                count = 0
            count+=1
            ptr+=1
        ans = 0
        for i in range(len(groups)-1):
            ans+=min(groups[i],groups[i+1])
            
        return ans
                
            
        