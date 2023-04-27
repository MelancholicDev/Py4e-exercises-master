fname = input("enter file name: ")
fhandle = open(fname)

dic = dict()
for line in fhandle:
    l = line.rstrip()
    if not line.startswith("From"):
        if len(l.split()) < 6:
            continue
    else:
        l = l.split()
        if len(l) > 6:
            hour = l[5].split(":")
            hour = hour[0]
            dic[hour] = dic.get(hour, 0) + 1
lis = list()
for (k, v) in dic.items():
    lis.append((k, v))
lis = sorted(lis)
for item in lis:
    print(item[0], item[1])
