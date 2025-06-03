class node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None               #starting point of linkedlist
        
    def insert_end(self, data):
        new_node=node(data)
        
        if(self.head is None):
            self.head=new_node       #links new node to head node
        else:
            temp=self.head
            
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def add_ll(self):                     #adding data
        temp=self.head
        sum=0
        while temp:
            sum = sum+temp.data
            temp=temp.next
        return sum

    def Count_ll(self):                  #counting data
        # code here
        count=0
        temp=self.head
        while temp:
            count = count+1
            temp=temp.next
        return count
    
    def insert_beginning(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def delete_beginning(self):
       self.head=self.head.next
       
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None

    def insert_position(self,pos,data):
        if pos==0:
            self.insert_beginning (data)
        else:
            new_node=node(data)
            temp=self.head
            for i in range(pos-1):
                if temp is None:
                    print("position out of bounds")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node

    def delete_position(self,pos):
        if pos == 0:
            self.delete_beginning()
        else:
            temp=self.head
            for i in range(pos-1):
                if temp.next is None:
                    print("position out of bounds")
                    return
            temp = self.head
        temp.next= temp.next.next
    def delete_value(self,value):
        if self.head.data==value:
           self.head=self.head.next 
           return
        temp=self.head
        while temp.next and temp.next.data !=value:
            temp = temp.next
        if temp.next is None:
            print("value not found")
            return
        temp.next= temp.next.next
    
        
        
        

ll=linkedlist()
ll.insert_end(10)
ll.insert_beginning(88888)
ll.insert_end(20)
ll.insert_end(30)
ll.display()
ll.delete_beginning()
ll.insert_end(40)
ll.display()
ll.delete_end()
ll.display()
ll.insert_position(3,700)
ll.display()
ll.delete_position(2)
ll.display()
ll.delete_value(20)
ll.display()


print("sum of the linkedlist is",ll.add_ll())
print("count of the linkedlist is",ll.Count_ll())
        
        
        
        
