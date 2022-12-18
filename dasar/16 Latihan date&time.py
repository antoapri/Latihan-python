import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"{hari_ini:%A}")
print("\n"+10*"="+"Latihan"+"="*10+"\n")

print("silakan masukan tanggl, bulan, dan tahun lahir anda")
tgl = int(input("Tanggal :"))
bln = int(input("Bulan \t:"))
thn = int(input("Tahun \t:"))

tgl_lahir = dt.date(thn,bln,tgl)
print("\n"f"tanggal lahir anda adalah = {tgl_lahir}")
hari_ini = dt.date.today()
print(f"hari ini tanggal = {hari_ini}"+"\n")

umur = hari_ini - tgl_lahir
umur_thn = umur.days // 365
umur_bln = (umur.days % 365) // 30

print(f"Hari Lahir Anda adalah = {tgl_lahir:%A}")
print(f"Umur Anda Adalah = {umur_thn} Tahun, {umur_bln} bulan""\n")
