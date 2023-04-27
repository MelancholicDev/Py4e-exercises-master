fname = input("enter file name: ")
fhandle = open(fname)
word_dic = dict()
words_list = list()
for line in fhandle:
    words_list = line.split()
    for word in words_list:
        word_dic[word] = word_dic.get(word, 0) + 1
