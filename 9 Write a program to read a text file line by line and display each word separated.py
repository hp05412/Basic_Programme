#Write a program to read a text file line by line and display each word separated by '#'.
fin=open(r"C:\Users\Dell\OneDrive\Desktop\text.txt",'r')
L1=fin.readlines( )
s=''
for i in range(len(L1)):
    L=L1[i].split( )
    for j in L:
        s=s+j
        s=s+'#'
print(s)
fin.close()
