fileSize = int(input("Enter the size of your file: "))
fileName = input("Enter the name of the file: ")

f = open(fileName, "w")

for x in range(fileSize):
    f.write('1')

f.close()