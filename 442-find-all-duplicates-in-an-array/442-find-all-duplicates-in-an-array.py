class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            element = abs(nums[i]) - 1
            if nums[element]<0:
                ans.append(element + 1)
            else:
                nums[element]*= -1
        return ans
                
                
        