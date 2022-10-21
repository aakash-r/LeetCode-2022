class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = {}
        p1 = 0
        p2 = 0
        maxl = 0
        curl = 0
        while p1<len(s) and p2<len(s):
            if s[p2] not in cur:
                cur[s[p2]] = p2
                curl+=1
                p2+=1
                maxl = max(maxl,curl)
            else:
                #print(p1,p2)
                while s[p1]!=s[p2]:
                    
                    del cur[s[p1]]
                    curl-=1
                    p1+=1
                cur[s[p1]] = p2
                p1+=1
                p2+=1
                
        return maxl
                
            
        
            
        