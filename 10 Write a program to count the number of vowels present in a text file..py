#Write a program to count the number of vowels present in a text file.
fin=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\vowel.txt",'r')
str=fin.read()
count=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
print(count)
fin.close()
