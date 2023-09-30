#Write a program to count number of words in a text file.
fin=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\vowel.txt",'r')
str=fin.read( )
L=str.split()
count_words=0
for i in L:
    count_words=count_words+1
print(count_words)
