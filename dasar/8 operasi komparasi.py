#setiap hasil dari operasi komparasi adalah boolean
#perator (>,<,>=,<=,==,!=,is,is not)

a = 5
b = 3
#lebih besar dari(>)
print("======> lebih besar dari(>)")
hasil = a > 3
print(a,">", 3, "=", hasil)
hasil = b > 2
print(b,">", 2, "=", hasil)
hasil = b > 3
print(b,">", 3, "=", hasil)
'''jika nilai pembading sama akan terjadi false 
karna mereka menghitu setelah nilai yang kita beri'''

#kurang dari (<)
print("======> kurang dari(<)")
hasil = a < 3
print(a,"<", 3, "=", hasil)
hasil = b < 2
print(b,"<", 2, "=", hasil)
hasil = b < 3
print(b,"<", 3, "=", hasil)

#lebih dari sama dengan(>=)
print("======> lebih dari sama dengan(>=)")
hasil = a >= 3
print(a,">=", 3, "=", hasil)
hasil = b >= 2
print(b,">=", 2, "=", hasil)
hasil = b >= 3
print(b,">=", 3, "=", hasil)
'''jika nilai pembading sama akan terjadi true
karna mereka menghitu mulai nilai ygang kita beri'''

#kurang dari sama dengan(<=)
print("======> kurang dari sama dengan(<=)")
hasil = a <= 3
print(a,"<=", 3, "=", hasil)
hasil = b <= 2
print(b,"<=", 2, "=", hasil)
hasil = b <= 3
print(b,"<=", 3, "=", hasil)

#sama dengan(==)
print("======> sama dengan(==)")
hasil = a == 5
print(a,"==", 5, "=", hasil)
hasil = b == 5
print(b,"==", 5, "=", hasil)
'''kalo (=) adsamen, kalo (==) membandingkan'''

#tidak sama dengan(!=)
print("======> sama dengan(!=)")
hasil = a != 5
print(a,"!=", 5, "=", hasil)
hasil = b != 5
print(b,"!=", 5, "=", hasil)


print("======> objek identity(is)")
#is sebagai komparasi objek identity
'''is dan is not berfungsi membandingkan memory objek'''
x = 5 #ini adalah assignment membuat objek
y = 5
print ('nilai x =',x,',id =',hex(id(x)))
print ('nilai y =',y,',id =',hex(id(y)))
hasil = x is y
print("x is y =",hasil)

x = 5 #ini adalah assignment membuat objek
y = 8
print ('nilai x =',x,',id =',hex(id(x)))
print ('nilai y =',y,',id =',hex(id(y)))
hasil = x is y
print("x is y =",hasil)


print("======> objek identity(is not)")
x = 5 #ini adalah assignment membuat objek
y = 5
print ('nilai x =',x,',id =',hex(id(x)))
print ('nilai y =',y,',id =',hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

x = 5 #ini adalah assignment membuat objek
y = 8
print ('nilai x =',x,',id =',hex(id(x)))
print ('nilai y =',y,',id =',hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

