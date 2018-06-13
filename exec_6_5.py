text = "X-DSPAM-Confidence:    0.8475";
if '0.8475' in text :
    atpos = text.find('0')
#    print (atpos)
    spos = text.find('5')
#    print (spos)
    num = text[atpos:spos+1]
    fnum = float(num)
    print(fnum)
else :
    print('Not found!')
