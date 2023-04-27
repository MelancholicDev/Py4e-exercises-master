fname = input("Enter file name: ")
fhandle = open(fname)
count = dict()
for line in fhandle:
    if not line.startswith("From"):
        continue
    else:
        splited_line = line.split()
        whole_address = splited_line[1]
        domain_name = whole_address.split("@")
        count[domain_name[1]] = count.get(domain_name[1], 0) + 1

print(count)
