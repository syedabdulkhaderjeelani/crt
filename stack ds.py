stack=[]
top=-1

def push(value):
    global top
    stack.append(value)
    top+=1
    
def pop( ):
    global top
    if(top==-1):
       print("stack is empty.nothing to pop")
       return
    else:
        stack.pop()
        top-=1
        
def peek():
    if top==-1:
        return "stack is empty.no top element"
    else:
        return f"top element={stack[top]}"
    
def display():
    if top==-1:
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
            
while True:
    choice=int(input("enter ur choice"))
    
    if choice==1:
       value=int(input("enter ele"))
       push(value)
       
    elif choice==2:
        pop()
        print(stack)
        pop()
        
    elif choice ==3:
        print(peek())
        
    elif choice ==4:
        display()
        
    else:
        print("exit")
        break
    
