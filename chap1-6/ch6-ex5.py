# exercise 5 from chapter 6 p4e:

stri = 'X-DSPAM-Confidence:0.8475'

# extract all after the colon character and then convert to a float:

colon = stri.find(':')
x = float(stri[colon+1:])
print(x, type(x))