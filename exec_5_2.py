largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        val = int(num)
    except :
#        print('Enter valid integer number')
        print('Invalid input')
        continue
    if largest is None :
        largest = val
    if smallest is None :
        smallest = val
    if val > largest :
        largest = val
    if val < smallest :
        smallest = val
print("Maximum is", largest)
print("Minimum is", smallest)
