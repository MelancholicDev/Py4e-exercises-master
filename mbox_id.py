fname = input("Enter File name: ")
try:
    fhandle = open(fname, "r")
except:
    print("Incorrect File name: ", fname)
    quit()
count = 0
for line in fhandle:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    else:
        count += 1
        splited_line = line.split()
        print(splited_line[1])
print(f"There were {count} lines in the file with From as the first word")
