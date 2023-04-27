fname = input("Enter file name: ")
fhandle = open(fname)
count = dict()
for line in fhandle:
    if not line.startswith("From"):
        continue
    else:
        splited_line = line.split()
        if len(splited_line) > 2:
            count[splited_line[2]] = count.get(splited_line[2], 0) + 1

print(count)
