# file handle fh
f = open('bioCorpus.txt')
# use readline() to read the first line
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
count = 0
nameList = []
s = 0
jobList = []
about = []
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    if line =='\n':
        count +=1
    else:
        count = 0
        s +=1
    if s ==1:
        nameList.append(line)

    if count == 0 and s ==2:
        jobList.append(line)

    if count >= 2:
        count =0
        s  = 0
    if s > 2:
        about.append(line)

    # use realine() to read next line
    line = f.readline()
f.close()
print(nameList)
print(jobList)
print(about)