#Write a menu based program to perform the operation on stack in python.
class Stack:
    def __init__(self):
    self.items = [ ]
    def isEmpty(self): # Checks whether the stack is empty or not
    return self.items == [ ]
    def push(self, item): #Insert an element
    self.items.append(item)
    def pop(self): # Delete an element
    return self.items.pop( )
    def peek(self): #Check the value of top
    return self.items[len(self.items)-1]
    def size(self): # Size of the stack i.e. total no. of elements in stack
    return len(self.items)
s = Stack( )
print("MENU BASED STACK")
cd=True
while cd:
 print(" 1. Push ")
 print(" 2. Pop ")
 print(" 3. Display ")
 print(" 4. Size of Stack ")
 print(" 5. Value at Top ")
 choice=int(input("Enter your choice (1-5) : "))

 if choice==1:
 val=input("Enter the element: ")
 s.push(val)
 elif choice==2:
 if s.items==[ ]:
 print("Stack is empty")
 else:
 print("Deleted element is :", s.pop( ))
 elif choice==3:
 print(s.items)
 elif choice==4:
 print("Size of the stack is :", s.size( ))
 elif choice==5:
 print("Value of top element is :", s.peek( ))
 else:
 print("You enetered wrong choice ")
 print("Do you want to continue? Y/N")
 option=input( )
 if option=='y' or option=='Y':
 var=True
 else:
 var=False
