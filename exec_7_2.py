# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
all = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pline = line.rstrip()
    atpos = pline.find('0')
    num = pline[atpos:]
    fnum = float(num)
    all = all + fnum
if count > 0 :
    print("Average spam confidence:",all/count)
