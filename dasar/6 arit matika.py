a = 10
b = 8
c = 3
print(5*"="+"perhitungan arit matika"+"="*5+"\n")
#penjumlahan
hasil = a+b
print (a,'+',b,'=',hasil)
#pengurangan
hasil = a-b
print (a,'-',b,'=',hasil)
#perkalian
hasil = a*b
print (a,'x',b,'=',hasil)
#pembagian
hasil = a/b
print (a,'/',b,'=',hasil)
#ekponen (pangkat) **
hasil = a**c
print (a,'**',c,'=',hasil)
#modulus (sisapembagian) %
hasil = a%c
print (a,'%',c,'=',hasil)
#floor division //
hasil = a//c
print (a,'//',c,'=',hasil)

print("\n"+5*"="+"prioritas"+"="*5)
#prioritas operasi 
'''
yang akan di selesaikan terlebih dahulu adalah ()
lalu exponen lalu perkalian,modulus,floor dan pembagian 
lalu penjumlahan dan penurangan
'''
''' 
    1. ()
    2. exponen **
    3. perkalian dll * / % ** //
    4. penjumlahan dan penurangan + -
'''
"""contoh1"""
hasil = a+c*b
print (a,'+',c,'*',b,'=',hasil)

"""contoh2"""
hasil = (a+c)*b
print (a,'+',c,'*',b,'=',hasil)