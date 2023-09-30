#Write a program to perform read and write operation with .csv file.
import csv
def readcsv():
    with open('C:\\Users\\ViNi\\Downloads\\data.csv','rt')as f:
    data = csv.reader(f) #reader function to generate a reader object
        for row in data:
print(row)
def writecsv( ):
    with open('C:\\Users\\ViNi\\Downloads\\data.csv', mode='a', newline='') as
file:
writer = csv.writer(file, delimiter=',', quotechar='"')
#write new record in file
writer.writerow(['4', 'Devansh', 'Arts', '404'])
print("Press-1 to Read Data and Press-2 to Write data: ")
a=int(input())
if a==1:
    readcsv()
elif a==2:
    writecsv()
else:
print("Invalid value")
