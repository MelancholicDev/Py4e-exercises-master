# This exercise contains and easter egg and finds the average spam confience
fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("File name is incorrect: ", fname)
    quit()
count = 0
sum = 0
for line in fhandle:
    line = line.rstrip()
    if not "X-DSPAM-Confidence" in line:
        continue
    else:
        count += 1
        x = line.find("0")
        sum += float(line[x:])
average = sum / count
print("Average Spam Confidence is : ", average)
