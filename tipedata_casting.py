# casting
# merubah tipe ke tipe lain

# INTEGER
print("=================INT============")
data_int = 9
print("data =", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # akan false jika nilai int = 0 dan akan true jika nilai int -1
print("data =", data_float, "type =",type(data_float))
print("data =", data_str, "type =",type(data_str))
print("data =", data_bool, "type =",type(data_bool))

## FLOAT
print("=================FLOAT============")
data_float = 9.9
print("data =", data_float, "type =",type(data_float))

data_int = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float) # akan false jika nilai int = 0 dan akan true jika nilai int -1
print("data =", data_int, "type =",type(data_int))
print("data =", data_str, "type =",type(data_str))
print("data =", data_bool, "type =",type(data_bool))

## BOOLEAN
print("=================BOOLEAN============")
data_bool = False;
print("data =", data_bool, "type =",type(data_bool))

data_int = int(data_bool)
data_str   = str(data_bool)
data_float  = bool(data_float) # akan false jika nilai int = 0 dan akan true jika nilai int -1
print("data =", data_int, "type =",type(data_int))
print("data =", data_str, "type =",type(data_str))
print("data =", data_float, "type =",type(data_float))

## STR
print("=================STR============")
data_str = "0";
print("data =", data_str, "type =",type(data_str))

data_int = int(data_str) # string harus angka
data_float  = float(data_str) # string harus angka
data_bool   = bool(data_str) # false jika string kosong
print("data =", data_int, "type =",type(data_int))
print("data =", data_float, "type =",type(data_float))
print("data =", data_bool, "type =",type(data_bool))