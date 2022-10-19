class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],x[1]))
        inter = intervals
        
        delete = 0
        curend = inter[0][1]
        for interval in inter[1:]:
            if interval[0]>=curend:
                curend = interval[1]
            else:
                delete+=1
                curend = min(curend,interval[1])
        return delete
        