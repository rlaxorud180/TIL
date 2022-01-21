class queue:
    
    def __init__(self, capacity):
        self.rear=0
        self.front=0
        self.count=0
        self.capacity=capacity
        self.que=[None]*capacity


    def is_full(self):

        return self.count==self.capacity

    def is_empty(self):

        return self.count==0


    def inque(self,value):
        if self.is_full():
            
            print("queue is full!")
            return False
        
        elif self.front==self.capacity-1 and self.front!=self.rear:
            self.que[self.front]=value
            self.front=0
            self.count=self.count+1
            print(self.rear,self.front,self.capacity)
            return value

            
        else:
            self.count=self.count+1
            self.que[self.front]=value
            self.front=self.front+1
            print(self.rear,self.front,self.capacity)
            return value

            
    def print_queue(self):
        return self.que

    
    def deque(self):
        
        if self.is_empty():
            print("queue is empty")
            return False

        
        
        elif self.front==self.capacity-1 and self.front!=self.rear:
            self.count=self.count-1
            tmp=self.que[self.rear]
            print("SDfsdfsd")
            self.que[self.rear]=None
            self.rear=0
            return tmp
            
        else:
            self.count=self.count-1
            tmp=self.que[self.rear]
            self.que[self.rear]=None    
            self.rear= self.rear+1
            print(self.rear,self.front,self.capacity)
        
            return tmp 
        
            
        

  
q=queue(4)
q.inque(1)
q.inque(1)
q.inque(1)
q.inque(1)

print(q.print_queue())
q.deque()
q.deque()
q.deque()
q.inque(1)
q.inque(1)

print(q.print_queue())        
        
