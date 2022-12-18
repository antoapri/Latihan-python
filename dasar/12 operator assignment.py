#operasi yang dapat dilakukan dengan penyingkatan
#operasi yang di tambahkan assignment

print("\n======Operasi Matamatika Biasa======\n")
a = 5#ini adalah assignment
print ("nilai a =",a)

##asssigment operator matamatika biasa
a +=1 #ini sama saja dengan a = a+1(operator tambah)
print ("nilai a += 1 , nilai a menjadi",a)

a -= 2 #ini sama saja dengan a = a-5(operator kurang)
print ("nilai a -= 2 , nilai a menjadi",a)

a *=5 #ini sama saja dengan a = a*5(operator kali)
print ("nilai a *= 5 , nilai a menjadi",a)

a /=2 #ini sama saja dengan a = a/5(operator kal/)
print ("nilai a *= 2 , nilai a menjadi",a)

##operator modulus
print("\n======Operator Modulus======\n")
b=10
print ("nilai b =",b)

b %=4
print ("nilai b %= 4, nilai b menjadi",b)
b=10
print ("nilai b =",b)

b //=3
print ("nilai b //= 3, nilai b menjadi",b)

a = 5#pangkat
print ("nilai a =",a)
a **=2
print ("nilai a **= 2, nilai a menjadi",a)

##operasi bitwise
print("\n======Operasi Operator Bitwise======\n")
#operasi OR
print("===Operasi or===")
c = True
print ("nilai C adalah :",c)
c |= False
print ("nilai c |= False, nilai c menjadi:",c)
c |= True
print ("nilai c |= True,  nilai c menjadi:",c)
c = False
print ("nilai C adalah :",c)
c |= False
print ("nilai c |= False, nilai c menjadi:",c)

print("\n===Operasi adn===\n")
c = True
print ("nilai C adalah :",c)
c &= True
print ("nilai c &= True,  nilai c menjadi:",c)
c &= False
print ("nilai c &= False, nilai c menjadi:",c)
c = False
print ("nilai C adalah :",c)
c &= False
print ("nilai c &= False, nilai c menjadi:",c)

print("\n===Operasi xor===\n")
c = True
print ("nilai C adalah :",c)
c ^= False
print ("nilai c ^= False, nilai c menjadi:",c)
c ^= True
print ("nilai c ^= True,  nilai c menjadi:",c)
c = False
print ("nilai C adalah :",c)
c ^= False
print ("nilai c &= False, nilai c menjadi:",c)

#shifting
print("\n===Operasi shifting===\n")
x = 0b00100
print ("nilai x adalah :",format(x,"05b"))
x >>= 2
print ("nilai x >>= 2, nilai x menjadi :",format(x,"05b"))
x <<= 3
print ("nilai x <<= 3, nilai x menjadi :",format(x,"05b"))

