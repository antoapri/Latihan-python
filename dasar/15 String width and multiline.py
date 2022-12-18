#data string
data_nama ="Anto"
data_umur =21
data_tinggi =168
data_berat =60

#string
data_string = f"nama={data_nama}, umur={data_umur}, tinggi={data_tinggi}, berat={data_berat}"
print(4*"="+"string"+"="*4)
print(data_string)

#string multiline menggunakan enter, new line (\n)
data_string = f"nama  = {data_nama} \numur  = {data_umur} \ntinggi= {data_tinggi} \nberat badan = {data_berat}"
print("\n"+4*"="+"string multiline (\\n)"+"="*4)
print(data_string)

#string multiline menggunakan 3 tanda kutip(""" """)
data_string = f"""
nama  = {data_nama} 
umur  = {data_umur}, tinggi badan = {data_tinggi}
berat badan  = {data_berat}
"""
print("\n"+3*"="+"string multiline menggunakan 3 kutip"+"="*3)
print(data_string)


#string multiline mengatur lebar
data_string = f"""
nama  = {data_nama} 
umur  = {data_umur} 
tinggi badan = {data_tinggi}
berat badan  = {data_berat}


nama  = {data_nama:>5} 
umur  = {data_umur:>5} 
tinggi badan = {data_tinggi:>4}
berat badan  = {data_berat:>4}


nama  = {data_nama:>11} 
umur  = {data_umur:>11} 
tinggi badan = {data_tinggi:>4}
berat badan  = {data_berat:>4}
"""
print("\n"+3*"="+"mengatur lebar dengan (>)"+"="*3)
print(data_string)
