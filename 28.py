# Latihan perulangan membuat segitiga

sisi = 10

# 1. menggunakan for

# dummy variabel
print("awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")

# 2. menggunakan while

print("awal while")
count = 1
while True:
    print("*"*count)
    count +=1

    if count > sisi:
        break

print("akhir while")

# 3. hanya ganjil saja

print("awal while")
count = 1
while True:
    # akan kembali ke atas jika ganjil 
    if (count%2):
        #print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
        
    #akan print jika genap
    if count > sisi:
        break 

print("akhir while")

# 4. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("akhir while")

angka = -1
while angka < 9:
    angka += 1
    if angka == 7:
        print("Angka ke 7 akan di skip")
        continue
    print("Angka perulangan --> ",angka)
    
        