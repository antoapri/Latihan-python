print ("\n Perhitungan Suhu \n")

#Celcius
cel = float(input("masukan suhu dalam sataun celcius: "))
print("suhu adalah:",cel,"Celcius")
#Reamur
ream = (4/5) * cel
print("celcius ke reamur: ",ream,"Reamur")
#Fahrenheit
fahr = ((9/5) * cel) + 32
print("celcius ke fahrenheit : ",fahr,"Fahrenheit")
#Kelvin
kel = cel + 273
print("celcius ke kelvin : ",kel,"kelvin")

print("===== Fahrenhet =====")
#fahrenheit ke kelvin
fah = float(input("masukan suhu dalam sataun fahrenheit :"))
print("suhu adalah:",fah,"F")
#celcius
ce = fah - (32 * (5/9))
print("fahrenheit ke celcius : ",ce,"C")
#Kelvin
fa = fah + (459.67 * (5/9))
print("fahrenheit ke kelvin : ",fa,"K")
#reamur
re = (4/9) * fah - 32
print("fahrenheit ke reamur : ",re,"R")

print("===== Kelvin =====")
#kelvin ke fahrenheit
kelvin = float(input("masukan suhu dalam sataun kelvin :"))
print("suhu adalah:",kelvin,"k")
#Celcius
ce = kelvin - 273.15
print("kelvin ke Celcius : ",ce,"C")
#fahrenheit
kelv = (kelvin * (9/5)) - 459.67
print("kelvin ke fahrenheit : ",kelv,"F")
#reamur
re = ((4/5) * kelvin) - 273
print("kelvin ke reamur : ",re,"R")
