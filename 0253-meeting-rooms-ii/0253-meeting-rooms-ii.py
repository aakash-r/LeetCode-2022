#MAXIMUM NO. OF INTERSECTING INTERVALS

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        s,e = 0,0
        ans = 0
        count = 0
        while s<len(start):
            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            ans = max(ans,count)
        
        return ans
            
        
        
        
        