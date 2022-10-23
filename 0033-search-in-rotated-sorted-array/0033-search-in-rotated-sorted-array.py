class Solution:
    def search(self, nums: List[int], t: int) -> int:
        def binary(l,r):
            if l>r: return -1
            mid = (l+r)//2
            if nums[mid]==t:
                return mid
            else:
                left = 0
                if nums[mid]>=nums[l]:
                    left = 1
                
                if left:
                    if t>nums[mid] or (t<nums[mid] and t<nums[l]):
                        return binary(mid+1,r)
                    elif t<nums[mid] and t>=nums[l]:
                        return binary(l,mid-1)
            
                if not left:
                    if t<nums[mid] or (t>nums[mid] and t>nums[r]):
                        return binary(l,mid-1)
                    elif t>nums[mid] and t<=nums[r]:
                        return binary(mid+1,r)
                    
        
        return binary(0,len(nums)-1)
        