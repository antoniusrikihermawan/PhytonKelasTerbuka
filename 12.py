
#GABUNGAN
inputdata = float(input("Masukkan Angka : "))
angka1 = (inputdata >= 0 and inputdata <= 5)
print(angka1)
angka2 = (inputdata >= 8 and inputdata <=11)
print(angka2)
hasilnya = angka1 or angka2
print("Jadi : ",hasilnya)

#IRISAN 
inputdata = float(input("Masukkan Angka : "))
angka1 = (inputdata <= 0 or inputdata >= 5)
print(angka1)
angka2 = (inputdata <= 8 or inputdata >= 11)
print(angka2)
hasilnya = angka1 or angka2
print("Jadi : ",hasilnya)





