# Break

# contoh 1

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang --> {angka}")

    if angka == 3:
        print("nice")
        break

    print("whatsups")

print("finish")

# contoh 2 

data_int = int(input("Hitung angka sampai = "))
angka = 0

while angka < data_int:
    angka += 1
    print(f"angka sekarang --> {angka}")

    if angka == data_int:
        print("nice")
        break

    print("what ups broku!") 

print("akhir dari program")