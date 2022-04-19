# operator dictionary

data_dict = {
    'key':'value',
    "kv":'kevin cy',
    "by":'bayu kntl',
    "aq":'ariq satan',
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang dari dictionary = {LENDICT}") 

# mengecek key exist atau tidak
KEY = "kv"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value atau (read) dengan menggunakan get
print(data_dict["kv"])
print(data_dict.get("by"))
print(data_dict.get("jmbd","Key tidak ditemukan")) # cek key message dengan tidak ditemukan

# mengupdate data
data_dict["aq"] = "setan"
print(data_dict)

# menambah data
data_dict["ry"] = "agus ryan"
print(data_dict)

data_dict.update({"kv":"kevin cyn"})
print(data_dict)
data_dict.update({"ozlow":"hoki"}) # kalo nilai tidak ada, maka di add.
print(data_dict)

# mendelete data pada dictionary
del data_dict["ozlow"]
print(data_dict)