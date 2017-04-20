import random
import re
filename = "mbox-anon.txt"
filename_1 = "mbox-anon-key.txt"
f = open("mbox.txt")
fp = f.readlines()
f_1 = open(filename, 'w')
f_2 = open(filename_1, 'w')
dic = {}

for line in fp:
    words = line.split()
    for i in words:
        i.replace('<','').replace('>','')
        if re.findall(r'^[a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', i) or re.findall(r'^[<](\D[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)[>]$',i):
            if i not in dic:
                a = random.randrange(10000,99999)
                if a not in dic.values():
                    dic[i] = a
                else:
                    dic[i]= random.randrange(10000,99999)
                f_2.write(str(dic[i]) + "=" + i)
                f_2.write("\n")
            line = line.replace(i, ("%%" + str(dic[i]) + "%%"))
    f_1.write(line)


print (len(dic.keys()))
