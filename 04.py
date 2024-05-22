# CASTING
# MERUBAH TIPE DATA KE TIPE DATA LAIN

print('=====INTEGER=====')
data_int = 9
print("data =", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int) # Kalau Value dari variabel 0 maka akan False 
print("data =", data_float, ",type =",type(data_float))
print("data =", data_string, ",type =",type(data_string))
print("data =", data_bool, ",type =",type(data_bool))

print('=====FLOAT=====')
data_float = 9.9
print("data = ", data_float, ",type =", type(data_float))

data_int = int(data_float)
data_string = str(data_float) # Akan dibulatkan ke bawah
data_bool = bool(data_float) # Kalau Value dari variabel 0 maka akan False
print("data =", data_int, ",type =", type(data_int) )
print("data =", data_string, ",type =", type(data_string))
print("data =", data_bool, ",type",type(data_bool))