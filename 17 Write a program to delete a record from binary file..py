#Write a program to delete a record from binary file.
import pickle
roll=input('Enter roll number whose record you want to delete:')
file=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\student.txt", "rb+")
list=pickle.load(file)
found=0
lst=[]
for x in list:
    if roll not in x['roll']:
        lst.append(x)
    else:
        found = 1
if found == 1:
    file.seek(0)
    pickle.dump(lst, file)
    print("Record Deleted ")
else:
    print('Roll Number does not exist')
file.close()
