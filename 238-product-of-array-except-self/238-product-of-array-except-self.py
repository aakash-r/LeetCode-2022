class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forw = [1]
        back = []
        cur = 1
        for i in nums:
            cur = cur*i
            forw.append(cur)
        
        cur = 1
        for i in nums[::-1]:
            cur = cur*i
            back.append(cur)
            
        back = back[::-1] 
        back = back[1:]
        back.append(1)
        forw = forw[:-1]
        #print(forw,back)
        return [i*j for i,j in zip(forw,back)]
            
        