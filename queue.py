class queue:
    def __init__(self,Q,value):
        self.Q=[]
        self.Q=Q
        self.value=value
        self.front=-1
        self.rare=-1
        
    def enqueue(self,Q,value):
        if(self.front==-1):
            self.front=0
        self.rare=self.rare+1
        #append it
        self.Q.append(value)
    def dequeue(self):
        #check for empty condition
        if self.is_empty():
            return "queue is empty"
        #delete element at front

        value=self.queue[self.front]
        self.front+=1
        if self.front>self.rear:
            self.front=self.rear=-1
            return value
    def is_empty(self):
        return self.front==-1 or self.front
    def size(self):
        if self.is_empty():
            return 0
        return self.rare-self.front+1
    def display(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print(self.q[self.front:self.rear+1])
#objects
q=queue

while True:
    choice=int(input("enter ur choice"))
    
    if choice==1:
        print(q.enqueue)
       
    elif choice==2:
        print(q.dequeue)
    elif choice ==3:
        print(q.is_empty)
    elif choice ==4:
       print (q.size)
    else:
        print("exit")
        break
    
