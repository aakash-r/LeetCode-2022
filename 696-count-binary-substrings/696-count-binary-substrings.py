class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zero = 0
        one = 0
        if s.count('0') == len(s) or s.count('1')==len(s):
            return 0
        zp = s.index('0')
        op = s.index('1')
        ans = 0
        while zp<len(s) and op<len(s):
            while zp<len(s) and s[zp]=='0':
                zero+=1
                zp+=1
            while op<len(s) and s[op]=='1':
                one+=1
                op+=1
            n = min(zero,one)
            zero = 0
            one = 0
            zp,op=op,zp
            ans += n
        return ans
                
            
        