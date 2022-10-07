class Solution:
    def isRobotBounded(self, ins: str) -> bool:
        directions = ['n', 'w', 's', 'e']
        cur = 0
        pos = [0,0]
        for i in ins:
            if i == 'G':
                if cur == 0:
                    pos[1]+=1
                elif cur == 1:
                    pos[0]-=1
                elif cur == 2:
                    pos[1]-=1
                elif cur == 3:
                    pos[0]+=1
            elif i=='L':
                cur = (cur+1)%4
            elif i=='R':
                cur = (cur-1)%4
        
        
        
        
        
        if pos == [0,0] or cur!=0: return True
        else: return False
                
            
        
        
        