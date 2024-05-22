# operasi logika atau boolean

# not, or, and, 
print('====NOT====')
a = False
c = not a 
print('data a =',a)
print('--------NOT')
print('data c =',c)

# 'OR' (jika salah satu TRUE maka hasilnya akan TRUE)
print('====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b 
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b 
print(a,'OR',b,'=',c)

# 'AND' (jika salah satu FALSE maka akan FALSE)
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR (jika salah satu TRUE maka akan TRUE)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b 
print(a,'XOR',b,'=',c)
a = True
b = True
print(a,'XOR',b,'=',c)




