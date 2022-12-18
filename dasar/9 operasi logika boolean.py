#operasi logika memiliki beberapa tanda yaitu
# not, or, adn, dan xor(^)

#not
print('====>not<====')
a =True
b =False
c = not a
print('data a =',a)
print('--------not')
print('data c =',c)
''' data (not) akan selalu menjadi kebalikan nya'''

#or
print('====>or<====')
a =True
b =True
c = a or b
print(a,' or',b,' =',c)
a =True
b =False
c = a or b
print(a,' or',b,'=',c)
a =False
b =True
c = a or b
print(a,'or',b,' =',c)
a =False
b =False
c = a or b
print(a,'or',b,'=',c)
'''(or) jika ada salah satu true maka pasti akan true, 
dan akan false jika keduanya nya false'''

#end
print('====>and<====')
a =True
b =True
c = a and b
print(a,' and',b,' =',c)
a =True
b =False
c = a and b
print(a,' and',b,'=',c)
a =False
b =True
c = a and b
print(a,'and',b,' =',c)
a =False
b =False
c = a and b
print(a,'and',b,'=',c)
'''(and) jika ada nilai false maka akan false, 
dan akan true jika kedua nilainya true'''

#xor
print('====>xor<====')
a =True
b =True
c = a ^ b
print(a,' xor',b,' =',c)
a =True
b =False
c = a ^ b
print(a,' xor',b,'=',c)
a =False
b =True
c = a ^ b
print(a,'xor',b,' =',c)
a =False
b =False
c = a ^ b
print(a,'xor',b,'=',c)
'''(xor) jika ada salah satu nilai true maka dia akan bernilai true,
dan jika ada nilai bernilai sama maka akan false'''