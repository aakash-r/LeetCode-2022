class CustomStack:
    size = 0
    stack = []
    maxSize = 0
    def __init__(self, maxSize: int):
        self.maxsize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if self.size+1<=self.maxsize:
            self.size+=1
            self.stack.append(x)
        

    def pop(self) -> int:
        if self.size>0:
            self.size-=1
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        c=0
        k = min(k,self.size)
        while c<k:
            
            self.stack[c]+=val
            c+=1
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)