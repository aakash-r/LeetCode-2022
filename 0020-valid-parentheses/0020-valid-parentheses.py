class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        for i in s:
            if i in ["(","{","["]:
                s1.append(i)
            elif i==')':
                if s1==[] or s1.pop()!='(': return False
            elif i=='}':
                if s1==[] or s1.pop()!='{': return False
            elif i==']':
                if s1==[] or s1.pop()!='[': return False
                
                
        if s1==[]: return True
        else: return False
        