unique_words = ['Arise', 'sick', 'soft', 'sun', 'the']
fname = input("Enter File name: ")
try:
    fhandle = open(fname, "r")
except:
    print("Incorrect File name: ", fname)
    quit()

for line in fhandle:
    line = line.rstrip()
    splited_string = line.split()
    for word in splited_string:
        if word not in unique_words:
            unique_words.append(word)
        else:
            continue
print(unique_words)
