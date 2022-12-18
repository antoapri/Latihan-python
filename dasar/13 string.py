data = "mencoba membuat string"
print(data)
print(type(data))

##jenis2 membuat SRT/string

'''
    1.kita bisa membuat string dengan menggunakan singgel quote ('_')
    2.juga bisa membuat string dengan menggunakan double quote ("_")
'''
#contoh
data = 'ini menggunakan singgel quote'
data = "ini menggunakan double quote"

#menggunakan tanda \
#backlash juga dianggap data kusus
#membuat kutip menjadi tanda string dangan di tambahkan (\)
print('selamat hari jum\'at')

#menggunakan double backlash
#contoh
print("C:\\user\\data")

#tab menggunakan \t
print("menggunakan \\t untuk tab: ini \tditab")

#backspace menggunakan \b
print("menggunakan \\b untuk backspace: ini \bdibackspace")

#newline menggunakan \n
print("menggunakan \\n untuk newline :ini bari pertama. \nini baris kedua.")
#menggunakan /r baris kedua pindah ke belakang
print("menggunakan \\r untuk newline :ini bari pertama. \rini baris kedua.")
#print("menggunakan untuk newline :ini bari pertama. \r\nini baris kedua.")

#string literal atau raw
#menggunakan row string dengan menambahkan (r)
print(r"C:\new\folder") 

#multiline literal string
print("""
kita
mencoba 
multiline literal 
String
""")

#multiline literal string dan raw
print(r"""
kita
mencoba 
multiline literal 
String
C:\new folder\tripang\nugat
""")

