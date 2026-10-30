# IMPLEMENT A STACK USING PYTHON

class Stack():
    
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)
        print(f"Pushed Item: {val}")

    def pop(self):
        if self.stack == []:
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.stack == []:
            return "Stack is Empty"
        print(self.stack[-1])

    def displayStack(self):
        print(f"Stack is: {self.stack}")


s=Stack()
s.push(10) 
s.push(20) 
s.push(30) 
s.push(40) 
s.push(50)
print("Displaying stack after pushing some elemnets")
s.displayStack()
s.pop() 
s.pop() 
s.pop() 
print("Displaying stack after poping some elemnets")
s.displayStack()

print("Displaying the top element")
s.peek()

s.pop()
s.displayStack()