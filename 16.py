# 1. Operasi dan Manipulasi String
nama_pertama = "Antonius"
nama_kedua = "Riki"
nama_ketiga = "Hermawan"

nama_lengkap = nama_pertama + " " + nama_kedua + "'" + nama_ketiga
print(nama_lengkap)

# 2. Operasi menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. Operator untuk string
#mengecek apakah ada komponen chaar atau string di string

h = "h"
status = h in nama_lengkap
print(h + "\tada di " + nama_lengkap + " = " + str(status))

H = "H"
status = H in nama_lengkap
print(H + "ada di " + nama_lengkap + " = " + str(status))

h = "h"
status = h not in nama_lengkap
print(h + "tidak ada di " + nama_lengkap + " = " + str(status))

# Mengulang String
print("Riki"*10)
print(10*"Riki")

# Indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6]) 
print("index ke-1 : " + nama_lengkap[-1])
print("index ke-2 : " + nama_lengkap[-2])
print("index ke-[0,3] " + nama_lengkap[0:3])
print("index ke-[2,6] " + nama_lengkap[2:6])
print("index ke-[0,2,4,6,8,10] " + nama_lengkap[0:11:2])

# Item paling kecil
print("paling kecil : " + min(nama_lengkap))

# Item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 120
print("ASCII code untuk 150 adalah " + chr(data))

# 4. Operator dalam bentuk Method

data = "antonius riki hermawan"
jumlah = data.count("o")
print("Jumlah o pada data adalah : " + data + " = " + str(jumlah))



