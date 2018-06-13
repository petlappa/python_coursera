#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#strip hour
hours = dict()

for line in handle :
    if 'From' in line :
        lista = line.split()
        if lista[0] == 'From' :
            #get time xx:yy:zz
            hline = lista[5]
            #split time with :
            line2 = hline.split(':')
            #store hour
            hours[line2[0]] = hours.get(line2[0],0) + 1

#list func from dictionary returns tuples
#that can be then sorted
t = list(hours.items())
t.sort()
#print hours in order each value key in own row
for k, v in t :
    print(k, v)
