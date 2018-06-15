name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_106096.txt"
handle = open(name)

import re
count = 0
sum = 0

for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for number in x :
            print('number: ',number)
            sum = sum + int(number)
        print(sum)
print('Done')
