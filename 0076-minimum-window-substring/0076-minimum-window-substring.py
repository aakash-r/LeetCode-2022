class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sdic = {}
        tdic = {}
        for i in s:
            sdic[i] = sdic.get(i,0) + 1
        for i in t:
            tdic[i] = tdic.get(i,0) + 1   
        for l,c in tdic.items():
            if sdic.get(l,0)<c:
                return ''
        
        l,r=0,0
        curtd = tdic.copy()
        cursd = {}
        curl = 0
        minl = None
        curstr = ''
        minstr=''
        while r<len(s) and l<len(s):
            if s[r] in tdic:
                cursd[s[r]] = cursd.get(s[r],0)+1
                if s[r] in curtd:
                    curtd[s[r]]-=1
                if curtd.get(s[r])==0:
                    del curtd[s[r]]
            
            if curtd == {}:
                curstr = s[l:r+1]
                if minstr == '':
                    minstr = curstr
                curl = r-l+1
                if minl is None:
                    minl = curl
                else:
                    minl = min(minl,curl)
                    
                while curtd=={}:
                    if s[l] in tdic:
                        cursd[s[l]]-=1
                        if cursd[s[l]]<tdic[s[l]]:
                            curtd[s[l]]=curtd.get(s[l],0)+1
                            curstr = s[l:r+1]
                            
                        if cursd[s[l]]==0:
                            del cursd[s[l]]
                    l+=1
                
                curl=r-l+1+1
                if curl<minl:
                    minl = curl
                    minstr = curstr
                    
                
            r+=1
        #print(minl,curl)  
        return (minstr)
            
                
            
            
        
        