class node:
    def __init__(self,prv,next,data):
        self.data=data
        self.next=None
        self.prv=None
        
class doublylinkedlist:
    def __init__(self):
        self.head=None               #starting point of linkedlist
        
    def insert_beginning(self, data):
        new_node=node(None,None,data)
        
        if(self.head is None):
            self.head=new_node       #links new node to head node
        else:
            new_node.next = self.head
            self.head.prv=new_node
            self.head=new_node

    def delete_beginning(self):
        self.head=self.head.next
        self.head.prv=None

       
    def delete_end(self):
        if self.head.next is None:
            self.head=None
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.prv.next=None

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

ll=doublylinkedlist()
ll.insert_beginning(10)
ll.insert_beginning(8)
ll.insert_beginning(20)
ll.insert_beginning(30)
ll.display()
ll.delete_beginning()
ll.display()
ll.delete_end()
ll.display()














    
