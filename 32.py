# teknik menduplikat list
a = ["riki", "widodo", "aris"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

#kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy
print("membuat list c dengan a.copy")
c = a.copy() # membuat data baru / full duplikat

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 0")
c[0] = "Dadang"
a[0] = "Anto"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


