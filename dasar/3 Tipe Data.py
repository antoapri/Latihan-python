#tipe data angka satuan yang tidak memiliki koama (int)
data = 1
print (type(data))
print ("data :",data)
print ("bertipe :", type(data))

#tipe data angka dengan koma (float)
data = 1.5
print (type(data))
print ("data :",data)
print ("bertipe :", type(data))

#tipe data kumpulan karakter (string)
data = "bambang"
print (type(data))
print ("data :",data)
print ("bertipe :", type(data))

#tipe data biner true/false (boolean)
data = True
print (type(data))
print ("data :",data)
print ("bertipe :", type(data))


#tipe data kusus
##bilangan kompleks
data = complex(6,3)
print (type(data))
print ("data :",data)
print ("bertipe :", type(data))

##tipe data dari bahasa C

#cara memanggil tipe data C
from ctypes import c_double

data = c_double(1.005)
print (type(data))
print ("data :",data)
print ("bertipe :", type(data))
