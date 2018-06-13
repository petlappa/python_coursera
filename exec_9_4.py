name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailers = dict()

count = 0
for line in handle :
    if 'From' in line :
        list = line.split()
        if list[0] == 'From' :
            count = count + 1
            mailers[list[1]] = mailers.get(list[1],0) + 1
#print(mailers)
bigcount = None
bigword = None
for word,count in mailers.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword, bigcount)
