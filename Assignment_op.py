# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5
print('nilai a',a)

# artinya adalah a = a + 1
a += 1
print('nilai a += 1, nilai a menjadi?',a)

a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2, nilai a menjadi?',a)

a *= 5 # artinya adalah a = a * 5
print('nilai a *= 2, nilai a menjadi?',a)

a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2, nilai a menjadi?',a)

b = 10
print('\nnilai b =',b)

# modulus dan floor division
b %= 3 # artinya adalah a = a / 2
print('nilai b %= 3, nilai a menjadi?',b)

b = 10
print('\nnilai b =',b)

b //= 3 # artinya adalah a = a / 2
print('nilai b //= 3, nilai a menjadi?',b)

# pangkat atau eksponen
a = 5
print('\nnilai a=',a)
a **= 3 # artinya adalah a = a / 2
print('nilai a **= 3, nilai a menjadi?',a)


# operasi bitwise
c = True
print('nilai c = ',c)
c |= False
print('nilai c |= False, maka nilai C menjadi?',c)
c = False
print('\nnilai C = ',c)
c |= False
print('nilai c |= False, maka nilai C menjadi?',c)

# AND
c = True
print('nilai c = ',c)
c &= False
print('nilai c &= False, maka nilai C menjadi?',c)
c = True
print('\nnilai C = ',c)
c &= True
print('nilai c &= True, maka nilai C menjadi?',c)

# XOR
c = True
print('nilai c = ',c)
c ^= False
print('nilai c ^= False, maka nilai C menjadi?',c)
c = True
print('\nnilai C = ',c)
c ^= True
print('nilai c ^= True, maka nilai C menjadi?',c)

# geser geser
d = 0b0100
print('\nnilai D = ',format(d,'04b'))
d >>= 2
print('nilai d >>= 2 maka nilai D menjadi?',format(d,'04b'))
d <<= 1
print('nilai d <<= 2 maka nilai D menjadi?',format(d,'04b'))