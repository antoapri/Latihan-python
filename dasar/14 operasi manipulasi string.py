print("\n",10*"=","string part1","="*10)
###operasi manipulasi string part1
#1. menyambungkan string
nama_depan="apri"
nama_tengah="anto"
nama_belakang="tri"

nama_lengkap = nama_depan + nama_tengah + " " + nama_belakang
print(nama_lengkap)

#2. menghitung panjang operator string
panjang = len(nama_lengkap)
print("panjang dari " +nama_lengkap+"= "+ str(panjang))

#3. operator untuk string
#mengecek apakah ada komponen char atau string dalam string
a = "a"
status = a in nama_lengkap
print("a " + a + "ada di "+ nama_lengkap +"= "+ str(status) )
a = "A"
status = a in nama_lengkap
print("A " + a + "ada di "+ nama_lengkap +"= "+ str(status) )
a = "A"
status = a not in nama_lengkap
print("A " + a + "tidak ada di "+ nama_lengkap +"= "+ str(status) )

#mengulang string
print(10*"HA")#bisa juga angka 10 di belakang
print("HA"*20)
print(5*"apa kabr ")

#indexing adalah kita mengabil data dari string dan kita poton2
print("index ke-0 :" +nama_lengkap[0]) 
print("index ke-1 :" +nama_lengkap[1]) 
print("index ke-2 :" +nama_lengkap[2]) 
print("index ke-3 :" +nama_lengkap[3])
#jika angka mines (-) akan mulai dari belakang
print("index ke-(-3) :" +nama_lengkap[-3])
print("index ke-(-2) :" +nama_lengkap[-2]) 
print("index ke-(-1) :" +nama_lengkap[-1]) 
#mengabil range 
print("index range ke-[0:4] :" +nama_lengkap[0:4])
#jika mau ngabil angka tengah aka depan harus di kurangi 1 
# contoh berikut
print("index range ke-[5:8] :" +nama_lengkap[5:8]) 
print("index range ke-[5:8] :" +nama_lengkap[4:8])
#mengabil dengan jeda
print("mengabi index ke-[0,2,4,6,8,10,12] :" +nama_lengkap[0:12:2]) 

#item paling kecil
print ("item paling keicl :" + min(nama_lengkap))
'''item paling kecil ada sepace'''
#item paling kecil
print ("item paling keicl :" + max(nama_lengkap))

#ascii code
ascii_code = ord("'")
print("ASCII code untuk spasi adalah " +str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))
#4 operator dalam membentuk method
data = "nugroho"
jumlah = data.count("o")
print ("jumlah O pada "+ data + "= " + str(jumlah))



###operasi manipulasi string Part2
##operator string methods
# merubah case dari srting
print("\n",10*"=","string part2","="*10,"\n")
# merubah semua ke upper case
salam = "APA Kabar BROoOoOoO!"
print("ini normal= "+salam)
salam = salam.upper()
print("ini diubah ke upper= "+salam)
#merubah semua menjadi lower
salam = salam.lower()
print("ini diubah ke lowe= "+salam)

#pengecekan dengan menggunakan (is)X methods
#contoh pengecekan islower() dan isupper() case
coba = "hello"
apakah_lower = coba.islower()
print(coba+" islower ="+ str(apakah_lower))#hasil pasti boolean
apakah_upper = coba.isupper()
print(coba+" isupper ="+ str(apakah_upper))#hasil pasti boolean

#contoh pengecekan isalpha() <==pengecekan semua huruf
# dan tidak kosa dan tidak angka 
coba1 = "apaajadah"
pengecekan_alpha = coba1.isalpha()
print(coba1+" isalpha ="+ str(pengecekan_alpha))
coba2 = "apa aja dah"
pengecekan_alpha = coba2.isalpha()
print(coba2+" isalpha ="+ str(pengecekan_alpha))#jika ada yg kosong atau space akan false
coba3 = "21apri1996"
pengecekan_alpha = coba3.isalpha()
print(coba3+" isalpha ="+ str(pengecekan_alpha))#jika ada angka juga akan false

#cohontoh pengecekan isalnum() <==pengecekan untuk huruf dan angka 
#biasanya digunakan untuk pengcekan password
coba4 = "Password123"
coba5 = "Ujian 2021"
pengecekan_alnum = coba4.isalnum()
print(coba4+" isalnum ="+ str(pengecekan_alnum))
pengecekan_alnum = coba5.isalnum()
print(coba5+" isalnum ="+ str(pengecekan_alnum))#jika ad yang kosong, jeda dan space akan false

#contoh pengecekan isdecimal() <== pengecekan untuk angka saja
coba6 = "20210922"
pengecekan_decimal = coba6.isdecimal()
print(coba6+" isdecimal ="+ str(pengecekan_decimal))

#contoh pengecekan isspace() <== pengecekan digunakan untuk tab,space, atau newline(\n)
coba7 = "   \n"
pengecekan_space = coba7.isspace()
print(coba7+" isdecimal ="+ str(pengecekan_space))

#contoh pengecekan istitle() <== pengecekan semua huruf besar pada awalan
coba8 = "Aprianto Tri Nugroho"
pengecekan_title = coba8.istitle()
print(coba8+" istitle ="+ str(pengecekan_title))

##contoh pengecekan startswith() dan endswith() 
cek_start = "Singkong goreng".startswith('Singkong')
print("start =" + str(cek_start))
#endswith()
cek_end = "Singkong goreng".endswith('goreng')
print("start =" + str(cek_end))

#penggabunagn komponen split() join()
#join()
pesan = ['aku','sayang','diri','ku']
print(pesan)
gabung = ' '.join(pesan)
print(gabung)
#split()
gabung ="aku sayang diri ku"
print(gabung.split(' '))

#alokasi karakter rjust(), ljust(), center()
#rjust()
kanan = "kanan".rjust(10,">")
print("'"+kanan+"'")
#ljust()
kiri = "kiri".ljust(10,"<")
print("'"+kiri+"'")
#center()
tengah = "tengah".center(10,"=")
print("'"+tengah+"'")

#strip() kebalikan dari ke-3nya menghilangkan karakter 
tengah = "tengah".strip("=")#menghilangkan karakter
print("'"+tengah+"'")


