class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = {}
        curl=0
        maxl = 0
        i = 0
        while i < len(s):
            if s[i] not in cur:
                cur[s[i]] = i
                curl += 1
                i+=1
            else:
                maxl = max(maxl,curl)
                curl = 0
                i = cur[s[i]]+1
                cur = {}
                
        return max(maxl,curl)
            
        