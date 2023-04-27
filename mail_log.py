fname = input("Enter file name: ")
fhandle = open(fname)
count = dict()
for line in fhandle:
    if not line.startswith("From"):
        continue
    else:
        splited_line = line.split()
        count[splited_line[1]] = count.get(splited_line[1], 0) + 1
big_count = None
big_sender = None

for sender, times in count.items():
    if big_count == None or times > big_count:
        big_count = times
        big_sender = sender
print(count)
print(f"{big_sender} : {big_count}")
