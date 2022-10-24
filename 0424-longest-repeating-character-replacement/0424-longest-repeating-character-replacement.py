class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cur = {}
        curl = 0
        l = 0
        maxc = 0
        maxlen = 0
        for r in range(len(s)):
            cur[s[r]] = cur.get(s[r], 0) + 1
            curl += 1
            maxc = max(maxc, cur[s[r]])
            
            while curl - maxc > k:
                cur[s[l]] -= 1
                curl -= 1
                l+=1
            maxlen = max(maxlen, curl)
        return maxlen
                    
            
            
            
            
        
        