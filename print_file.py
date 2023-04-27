fname = input("Enter the file's name: ")
fhandle = open(fname)
for line in fhandle:
    line = line.rstrip()
    print(line.upper())
