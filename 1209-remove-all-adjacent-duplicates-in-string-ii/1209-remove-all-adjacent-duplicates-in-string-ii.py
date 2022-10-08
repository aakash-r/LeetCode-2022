class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if len(stack)>0 and stack[-1][0] == i:
                stack[-1][1]+=1
            else:
                stack.append([i,1])
            if stack[-1][1]==k:
                stack.pop()
        #print(stack)
        return "".join([i[0]*i[1] for i in stack])
            
        