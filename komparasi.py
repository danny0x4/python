# Operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not
# = adalah assigment, == adalah membandingkan nilai a dan b
a = 4
b = 2

# lebih besar dari >
print("====LEBIH BESAR====")
hasil = a > 3
print(a,'>',3,'=',hasil)

hasil = b > 3
print(b,'>',3,'=',hasil)

hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print("====LEBIH BESAR====")
hasil = a < 3
print(a,'<',3,'=',hasil)

hasil = b < 3
print(b,'<',3,'=',hasil)

hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari <
print("====LEBIH DARI SAMA DENGAN====")
hasil = a >= 3
print(a,'>=',3,'=',hasil)

hasil = b >= 3
print(b,'>=',3,'=',hasil)

hasil = b >= 2
print(b,'>=',2,'=',hasil)

# lebih dari <
print("====KURANG DARI SAMA DENGAN====")
hasil = a <= 3
print(a,'<=',3,'=',hasil)

hasil = b <= 3
print(b,'<=',3,'=',hasil)

hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan
print("====SAMA DENGAN====")
hasil = b == 4
print(b,'==', 4,hasil)
hasil = a == 4
print(a,'==', 4,hasil)

# sama dengan
print("====TIDAK SAMA DENGAN====")
hasil = b != 4
print(b,'!=', 4,hasil)
hasil = a != 4
print(a,'!=', 4,hasil)

# 'is' sebagai komparasi object identity

print("====OBJECT IDENTITY IS====")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)