#list
from xml.sax import default_parser_list


data_angka = [1,2,3,4,5]
print(data_angka)

# data string
data_string = ["aku","kamu","kita"]
print(data_string)

# data campuran
data_campuran = [1,"aku",2,"kita",3,"kamu"]
print(data_campuran)

data_boolean = [True,False,True,True]
print(data_boolean)

data_range = range(0,10)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_dgn_for = [i**2 for i in range(0,10)]
print(list_dgn_for)

list_pakai_for_if = [i for i in range(0,10) if i != 5]
print(list_pakai_for_if)

#genap
list_pakai_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pakai_for_if)

#ganjil
list_pakai_for_if = [i**2 for i in range(0,10) if i%2 != 0]
print(list_pakai_for_if)