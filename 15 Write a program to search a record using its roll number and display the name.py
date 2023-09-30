# Write a program to search a record using its roll number and display the name of student. If record not found then display appropriate message.
import pickle
roll=input('Enter roll number that you want to search in binary file :')
file=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\student.dat","rb")
list=pickle.load(file)
for x in range(10):
    if roll in list['roll']:
        print("Name of student is:",list['name'])
    break
else:
    print("Record not found")
file.close()
[45,35,3532]
