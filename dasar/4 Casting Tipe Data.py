#casting tipe data
#casting adalah merubah tipe data 
#tipe data: int, str, float, boolean
print("====INT====")
data_int: int
data_int = 8;
print ("data =", data_int, ",type =",type(data_int))
#casting int
data_str = str(data_int)
data_float = float(data_int)
data_bool = bool(data_int) #akan aflse jika nilai int 0
print ("data =", data_str, ",type =",type(data_str))
print ("data =", data_float, ",type =",type(data_float))
print ("data =", data_bool, ",type =",type(data_bool))

print("====STR====")
data_str = "80";
print ("data =", data_str, ",type =",type(data_str))
#casting str
data_int = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka 
data_bool = bool(data_str) #akan false string kosong
print ("data =", data_int, ",type =",type(data_int))
print ("data =", data_float, ",type =",type(data_float))
print ("data =", data_bool, ",type =",type(data_bool))
#jika str dikosongkan maka int dan float aka error
print("==STR kosong maka boolean akan false==")
data_str = "";
print ("data =", data_str, ",type =",type(data_str))
data_bool = bool(data_str) #akan false string kosong
print ("data =", data_bool, ",type =",type(data_bool))

print("====float====")
data_float = 8.5;
print ("data =", data_float, ",type =",type(data_float))
#casting float
data_int  = int(data_float) #akan dibulatkan ke bawah 
data_str  = str(data_float) 
data_bool = bool(data_float) #akan false jika float 0 
print ("data =", data_int, ",type =",type(data_int))
print ("data =", data_str, ",type =",type(data_str))
print ("data =", data_bool, ",type =",type(data_bool))

print("====boolean true====")
data_bool = True;
print ("data =", data_bool, ",type =",type(data_bool))
#casting boolea
data_int  = int(data_bool)  
data_str  = str(data_bool) 
data_float = float(data_bool)  
print ("data =", data_int, ",type =",type(data_int))
print ("data =", data_str, ",type =",type(data_str))
print ("data =", data_float, ",type =",type(data_float))
print("====boolean False====")
data_bool = False;
print ("data =", data_bool, ",type =",type(data_bool))
#casting boolea
data_int  = int(data_bool)  
data_str  = str(data_bool) 
data_float = float(data_bool)  
print ("data =", data_int, ",type =",type(data_int))
print ("data =", data_str, ",type =",type(data_str))
print ("data =", data_float, ",type =",type(data_float))
print("====boolean angka====")
data_bool = 80.5;
print ("data =", data_bool, ",type =",type(data_bool))
#casting boolea
data_int  = int(data_bool)  
data_str  = str(data_bool) 
data_float = float(data_bool)  
print ("data =", data_int, ",type =",type(data_int))
print ("data =", data_str, ",type =",type(data_str))
print ("data =", data_float, ",type =",type(data_float))