#PROVIDE THE INPUT FILE
#For example D:\EMBL\Assignment2\Workbook\InputB_Q1.txt

inFile=input("Enter the input file with full path\n")
f1=open(inFile,'r')
outFile=open('Unique.out','w')
getInput=f1.readlines()

list=[]

for line in getInput:
  if (line.strip() not in list):
     list.append(line.strip())
     outFile.write(line)

outFile.close() 