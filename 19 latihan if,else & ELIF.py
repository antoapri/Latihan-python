#LATIHAN
print ("""+++ini adalah operator+++
penjumlahan: +
pengurangan: -
perkalian  : x
pembagian  : /
pangkat    : ^ """)
print (5*"="+"Kalkulator Sederhana"+"="*5+"\n")
try:
    angka_1 = float(input("masukan angka pertama: "))
    operator = input("masuakn operator:")
    angka_2 = float(input("masukan angka kedua: "))


#opersai percabangan
    if operator == "+":
        hasil = angka_1 + angka_2
        print (f"hasilnya adalah:{hasil}")
    elif operator == "-":
        hasil = angka_1 - angka_2
        print (f"hasilnya adalah: {hasil}")
    elif operator == "x":
        hasil = angka_1 * angka_2
        print (f"hasilnya adalah:{hasil}")
    elif operator == "/":
        hasil = angka_1 / angka_2
        print (f"hasilnya adalah:{hasil}")
    elif operator == "^":
        hasil = angka_1 ** angka_2
        print (f"hasilnya pangkat adalah:{hasil}")
    else :
        print ("ERROR....!!!! Operator yang anda masukan tidak dimengerti.")
except:
    print ("ERROR....!!!! anda tidak memasukan angka dengan benar!!!")
    
print("selesai Terima Gaji")