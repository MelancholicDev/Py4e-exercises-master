fname = input("enter file name: ")
fhandle = open(fname)

dic = dict()
for line in fhandle:
    l = line.rstrip()
    if not line.startswith("From"):
        continue
    else:
        l = l.split()
        address = l[1]
        dic[address] = dic.get(address, 0) + 1
lis = list()
for (k, v) in dic.items():
    lis.append((v, k))
lis = sorted(lis, reverse=True)
print(lis[0][1], lis[0][0])
