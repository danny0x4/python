# looping dictionary

kawan = {
    'kv':'kevin cyn',
    'by':'bayu jawa',
    'aq':'ariq satan',
    'ry':'agus pro',
}

# looping first try (yang keluar adalah key)

for temen in kawan:
    print(temen)


# operator untuk mengambil item / iterables
keys = kawan.keys()
print(keys)

for key in kawan:
    print(kawan.get(key))

values = kawan.values()
print(values)

for value in kawan.values():
    print(value)

items = kawan.items()
print(items)

for item in kawan.items():
    print(item)

for key,value in kawan.items():
    print(f"Key = {key}, value = {value}")