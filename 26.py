# continue pass break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5 :
    angka += 1
    if angka == 3 :
        pass #ini tidak akan dieksekusi
    print(angka)

# continue 

angka = 0

while angka < 5 :
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice")
        continue # akan mmebuat loop meloncat ke angka selanjutnya

    print("what ups broku!") #aksi 2
print("finish")
