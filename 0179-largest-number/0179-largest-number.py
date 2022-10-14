from functools import cmp_to_key

def compare(x,y):
    if x==y:
        return 0
    elif x+y>y+x:
        return 1
    else:
        return -1
    
class Solution:
    
        
        
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums)==0:
            return "0"
        nums = [str(i) for i in nums] 
        nums = sorted(nums, key = cmp_to_key(compare), reverse=True)
        #print(nums)
        return ''.join([str(i) for i in nums])