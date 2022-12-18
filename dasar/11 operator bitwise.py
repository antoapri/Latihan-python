#operator bitwise atau biner atau binary

a =10
b =8

#bitwise OR (|)
c = a|b
print ("\n====(OR)====")
print ("nilai :",a,", binary :",format(a,"08b"))
print ("nilai :",b," , binary :",format(b,"08b"))
print ("==========>OR(|)")
print ("nilai :",c,", binary :",format(c,"08b"))

#bitwise AND (&)
c = a&b
print ("\n====(AND)====")
print ("nilai :",a,", binary :",format(a,"08b"))
print ("nilai :",b," , binary :",format(b,"08b"))
print ("==========>AND(&)")
print ("nilai :",c,", binary :",format(c,"08b"))

#bitwise XOR (^)
c = a^b
print ("\n====(XOR)====")
print ("nilai :",a,", binary :",format(a,"08b"))
print ("nilai :",b," , binary :",format(b,"08b"))
print ("==========>XOR(^)")
print ("nilai :",c,", binary :",format(c,"08b"))

#bitwise NOT (~)
c = ~b
print ("\n====(NOT)====")
print ("nilai :",b,", binary :",format(b,"08b"))
print ("==========>NOT(~)")
print ("nilai :",c,", binary :",format(c,"08b"))
print ("==========>XOR(^)")
d = 0b00001000
e = 0b11111111
print ("nilai :",e^d,", binary :",format(e^d,"08b"))

#shifting
#shifting ke kanan (>>)
c = b >> 2
print ("\n====(shifting)====")
print ("nilai :",b,", binary :",format(b,"08b"))
print ("==========>kanan 2x(>>)")
print ("nilai :",c,", binary :",format(c,"08b"))

#shifting ke kiri (<<)
c = b << 1
print ("\n====(shifting)====")
print ("nilai :",b,", binary :",format(b,"08b"))
print ("==========>kanan 1x(<<)")
print ("nilai :",c,", binary :",format(c,"08b"))
