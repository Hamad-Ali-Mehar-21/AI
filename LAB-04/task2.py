# IMPLEMENT A QUEUE USING PYTHON

class Queue():
    
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)
        print(f"Pushed Item: {val}")

    def dequeue(self):
        if self.queue == []:
            return "Queue is Empty"
        return self.queue.pop(0)
    
    def front(self):
        if self.queue == []:
            return "Queue is Empty"
        print(self.queue[0])

    def displayQueue(self):
        print(f"Queue is: {self.queue}")


q=Queue()
q.enqueue(10) 
q.enqueue(20) 
q.enqueue(30) 
q.enqueue(40) 
q.enqueue(50)
print("Displaying queue after pushing some elemnets")
q.displayQueue()
q.dequeue() 
q.dequeue() 
q.dequeue() 
print("Displaying queue after poping some elemnets")
q.displayQueue()

print("Displaying the top element")
q.front()
