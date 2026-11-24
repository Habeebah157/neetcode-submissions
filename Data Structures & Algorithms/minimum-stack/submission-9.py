class MinStack:
    #So how is this supposed to work. 
    #When the function is called how does that work?
    # When I place . 
    #What does the init function do?
    # Start the function
    

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        if (self.stack):
            self.stack.pop()
        if (self.minstack):
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        print(self.minstack)
        if(self.minstack):
            return self.minstack[-1]
        else:
            return 0
        
