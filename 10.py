#OPERASI KOMPARASI
a = 4
b = 2

#lebih besar dari
print('===============lebih besar dari (>)')
hasil = a > 3
print(a,">",3,'=',hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > b
print(b,">",b,"=",hasil)

#kurang dari
print('===============kurang dari (<)')
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < b
print(b,"<",b,"=",hasil)

#lebih dari sama dengan
print('================lebih dari sama dengan (>=)')
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= b
print(b,">=",b,"=",hasil)

#kurang dari sama dengan
print('================kurang dari sama dengan (<=)')
hasil = a <= 3
print(a,"<=",a,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= b
print(b,"<=",b,"=",hasil)

#sama dengan (==)
print('=================sama dengan (==)')
hasil = a == a
print(a,"==",a,"=",hasil)
hasil = a == b
print(a,"==",b,"=",hasil)

#tidak sama dengan (!=)
print('==================tidak sama dengan')
hasil = a != 4
print(a,"!=","=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

# 'is' sebagai komparasi object identity
x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(id)))
hasil = x is y
print('x is y =',hasil)







