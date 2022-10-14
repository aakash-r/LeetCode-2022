from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = [[-c,charr] for charr,c in count.items()]
        # print(h)
        heapq.heapify(h)
        # print(h)
        ans = ''
        prev = None
        while h:
            high = heapq.heappop(h)
            ans+=high[1]
            if prev is not None:
                heapq.heappush(h, prev)
            
            if high[0]+1<0:
                prev = [high[0]+1,high[1]]
            else:
                prev = None
        if prev is not None:
            if prev[1]!=ans[-1]:
                ans+=prev[1]
            else:
                return ''
            
        return ans
            
        
        