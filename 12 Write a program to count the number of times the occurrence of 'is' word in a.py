#Write a program to count the number of times the occurrence of 'is' word in a text file.
fin=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\vowel.txt",'r')
str=fin.read( )
L=str.split( )
count=0
for i in L:
    if i=='is':
        count=count+1
print(count)
fin.close( )
