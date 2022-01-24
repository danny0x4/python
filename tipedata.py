data_integer = 1

print("data :", data_integer)
print("- bertipe : ", type(data_integer))

#tipe data float untuk angka koma
data_float = 1.5
print("data :", data_float)
print("- bertipe: ", type(data_float))

#tipe data string atau karakter
data_string = "ucup"
print("data :", data_string)
print("- bertipe: ", type(data_string))

#tipe data boolean true/false
data_bool = True
print("data :", data_float)
print("- bertipe ", type(data_bool))

# bilangan kompleks (j itu imajiner)
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe ", type(data_c_double))