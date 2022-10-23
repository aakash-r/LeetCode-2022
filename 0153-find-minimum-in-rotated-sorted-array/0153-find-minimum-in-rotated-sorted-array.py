class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        def binary(l,r):
            if l>r: return
        
            mid = (l+r)//2
            
            if l==r: return mid
            
            elif mid!=0 and nums[mid]<nums[mid-1]: return mid
            
            elif nums[l]<=nums[mid]<=nums[r]: return l
            
            else:
                left = 0
                if nums[mid]>=nums[0]:
                    left = 1

                if left:
                    return binary(mid+1,r)
                elif not left:
                    return binary(l,mid)
            
        return nums[binary(0,len(nums)-1)]
            
                
            
                
            
                
        