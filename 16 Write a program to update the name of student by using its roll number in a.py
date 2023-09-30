#Write a program to update the name of student by using its roll number in a binary file.
import pickle
roll=input('Enter roll number whose name you want to update in binary file :')
file=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\student.txt", "rb")
list=pickle.load(file)
found=0
lst=[]
for x in list:
    if roll in x['roll']:
        found=1
        x=x['name']
        x=input('Enter new name: ')
    lst.append(x)
if found==1:
    file.seek(0)
    pickle.dump(lst,file)
    print("Record Updated")
else:
    print('roll number does not exist')
file.close( )
