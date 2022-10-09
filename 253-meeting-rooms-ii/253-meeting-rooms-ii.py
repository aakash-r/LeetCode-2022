class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #intervals.sort(key = lambda x: x[0])
        times = []
        for i in intervals:
            times.append([i[0],'s'])
            times.append([i[1],'e'])

        times.sort(key = lambda x: (x[0],x[1]))
        c = 0
        mm = 0
        for i in times:
            if i[1] == "s":
                c+=1
            else:
                c-=1
            
            mm = max(c,mm)
            
        return mm
            
        
        