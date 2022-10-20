class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ans = set()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            start = i+1
            end = len(nums) - 1

            while start<end:
                if nums[start]+nums[end]==target:
                    ans.add(tuple(sorted([nums[i],nums[start],nums[end]])))
                    start+=1
                elif nums[start]+nums[end]<target: start+=1
                else: end-=1
        return [list(i) for i in ans]
        