#Create a binary file with name and roll number of student and display the data by reading the file.
import pickle
def writedata( ):
    list =[ ]
    while True:
        roll = input("Enter student Roll No:")
        sname = input("Enter student Name :")
        student = {"roll":roll,"name":sname}
        list.append(student)
        choice= input("Want to add more record(y/n) :")
        if(choice=='n'):
            break
file = open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\student.txt","wb")
pickle.dump(list,file)
file.close( )
def readdata( ):
    file = open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\student.txt", "rb")
    list = pickle.load(file)
    print(list)
file.close( )
print("Press-1 to write data and Press-2 to read data")

choice=int(input( ))
if choice==1:
    writedata( )
elif choice==2:
    readdata( )
else:
    print("You entered invalid value")
