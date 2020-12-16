#PROVIDE THE INPUT FILE
#D:\EMBL\Assignment2\Workbook\InputB_Q1.txt

inFile=input("Enter the input file with full path\n")
f1=open(inFile,'r')
outFile=open('NoDup.out','w')
getInput=f1.readlines()

# Script is using python set method to remove duplicates. Set only accepts unique entries
content=set(getInput)
print(content)

for line in content:
      print(line)
      outFile.write(line)

outFile.close()