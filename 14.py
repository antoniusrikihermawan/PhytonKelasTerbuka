# opersi yang dapat dilakukan dengan penyingkatan
# opersi ditambah dengan assigment

a = 5 # adalah assigment
print('nilai a = ',a)

a += 1 # artinya adalah a = a + 1
print('nilai a += 1, nilai a menjadi : ',a)

a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2, nilai a menjadi : ',a)

a *= 2 # artinya adalah a = a * 2
print('nilai a *= 2, nilai a menjadi : ',a)

a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2, nilai a menjadi : ',a)

b = 10 
print('\nnilai b = ',b)

# modulus dan floor devision
b %= 3
print('nilai b %= 3, nilai b menjadi : ',b)

b = 10 
print('\nnilai b = ',b)

# pangkat atau eksponen
b //= 3
print('nilai b //=3, nilai b menjadi = ',b)

a = 5 
print('\nnilai a = ',a)

a **= 3
print('nilai a **= 3, nilai a menjadi = ',a)

# operator bitwise
# OR
c = True
print('\nnilai c = ',c)
c |= False
print('nilai c |= False, nilai c menjadi',c)
c = False
print('nilai c = ',c)
c |= False
print('nilai c |= False, nilai menjadi ',c)

# AND
c = True
print('\nnilai c = ',c)
c &= False
print('nilai c &= False, nilai c menjadi',c)
c = True
print('nilai c = ',c)
c &= True
print('nilai c &= False, nilai menjadi ',c)

# OR
c = True
print('\nnilai c = ',c)
c ^= False
print('nilai c ^= False, nilai c menjadi',c)
c = True
print('nilai c = ',c)
c ^= True
print('nilai c ^= False, nilai menjadi ',c)

# geser geser
d = 0b0100
print('\nnilai d = ',format(d,'04b'))
d >>= 2
print('nilai d >>= 2, nilai d menjadi =',format(d,'04b'))
d <<= 1
print('nilai d <<= 2, nilai d menjadi =',format(d,'04b'))






