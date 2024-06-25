data_angka = [1,23,3,45,5,56,75,34,56,4,532,2,34]

print(f"data angka = {data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data 
data = ["Ucup", "Otong", "Dudung", "Ujang"]
print(f"data = {data}")

index_Otong = data.index("Dudung")
index_Ujang = data.index("Ujang")
print(f"index Otong = {index_Otong}")
print(f"index Ujang = {index_Ujang}")

# mengurut list angka
print(f"data angka sebelum diurutkan {data_angka}")
data_angka.sort()
print(f"data angka saat diurutkan = {data_angka}")

print(f"data nama sebelum diurutkan {data}")
data.sort()
print(f"data nama saat diurutkan = {data}")

# membalikkan data list
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")

