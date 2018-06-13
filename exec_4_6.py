def computepay(h,r):
    return ((40*r)+((h-40)*r*1.5))

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h <= 40 :
    p = h*r
else :
    p = computepay(h,r)

#p = computepay(10,20)
#print("Pay",p)
print (p)
