#Write a program to write those lines which have the character 'p' from one text file to another text file.
fin=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\vowel.txt","r")
fout=open(r"C:\Users\Dell\OneDrive\Desktop\Class 12\CS\PRACTICAL\vowel.txt","a")
a=fin.readlines( )
for j in a:
    if 's' in j:
        fout.write(j)
fin.close()
fout.close()
