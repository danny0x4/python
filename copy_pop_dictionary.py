# copy dictionary

kawan = {
    'by':'bayu',
    'aq':'ariq',
    'kv':'kevin',
    'ag':'agil',
    'as':'ryan',
}

friends = kawan.copy() # agar tidak kerubah semuanya
print(f"ini adalah kawan: {kawan}\n")
print(f"ini adalah friends: {friends}\n")

kawan ['by'] = 'bayu qmack'
print(f"ini adalah kawan: {kawan}\n")
print(f"ini adalah friends: {friends}\n")

# pop dictionary (berdasarkan key)
data_ryan = friends.pop("ag")
print(f"Data ryan = {data_ryan}\n")
print(f"friends = {friends}\n")

# popitem dictionary (mengambil data terakhir)
dataTerakhir = friends.popitem()
print(f"Data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")