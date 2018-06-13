#use romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
flst = list()

for line in fh:
    line.rstrip()
#    print(line.rstrip())
    # split line into words
    lst = line.split()
    # check if word exists and add if not
#    print(lst)
    for word in lst :
        if word not in flst :
            flst.append(word)
flst.sort()
print(flst)
