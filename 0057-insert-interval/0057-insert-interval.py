class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        ans = []
        done = 0
        for i in range(len(intervals)):
            
            if new[1]<intervals[i][0]:
                ans.append(new)
                return ans+intervals[i:]
                
            elif new[0]>intervals[i][1]:
                ans.append(intervals[i])
            else:
                new = [min(new[0],intervals[i][0]), max(new[1],intervals[i][1])]
                
        
        ans.append(new)
        return ans
             
            