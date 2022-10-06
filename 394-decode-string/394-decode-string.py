class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        cur = ''
        stack = []
        curnum = ''
        for i in s:
            #print(i,stack, cur, ans)
            if i.isdigit():
                curnum+=i
            elif i == '[':
                if cur!='':
                    stack.append(cur)
                    cur=''
                stack.append(curnum)
                curnum = ''
            elif i.isalpha():
                cur+=i
            elif i==']':
                
                while True:
                    if stack[-1].isalpha():
                        cur = stack.pop() + cur
                    elif stack[-1].isdigit():
                        n = int(stack.pop())        
                        cur = cur*n
                        break
                #stack.append(ans)
                #ans = ''
                
                
                
        return ''.join(stack) + cur
        