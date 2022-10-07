class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if (n<0 and d>0) or (n>0 and d<0):
            final = '-'
        else:
            final = ''
        n = abs(n)
        d = abs(d)
        cur = ''
        dic = {}
        rem = (n%d)
        quot = n//d
        dec = ''
        dic[rem] = 1
        rep = -1
        counter=0
        while rem>0:
            counter+=1
            rem = rem*10
            if d>rem:
                
                dec+='0'
                continue
            q = rem//d
            rem = (rem%d)
            dec+=str(q)
            if rem == 0:
                break
            elif dic.get(rem,-1)!=-1:
                rep = str(((rem)*10)//d)
                break
            else:
                dic[rem] = 1
        print(quot,dec, rep)
        if rep != -1:
            for i in range(len(dec)):
                if dec[i]==rep:
                    dec = dec[:i]+'('+dec[i:]+')'
                    break
        if dec=='':
            return final + str(quot)
        else:
            return final + str(quot)+'.'+dec
            