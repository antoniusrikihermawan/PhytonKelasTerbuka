# Operasi 

# index 0(-3) 1(-2) 2(-1)

data = ["riki", "anton", "aris"]

# mengambil data dari list ini 
data_0 = data[0]
print(f"data pertama (index 0) {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) {data_terakhir}")

data_riki = data[-3]
print(f"data riki (index -3) {data_riki}")

# mengambil info jumalh data dalam list 
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list 
print(f"data sebelum di tambahkan {data}")
data.insert(1,"widodo")
print(f"data sesudah di tambahkan di indek ke 2 = {data}")

# menambahkan data di akhir list
data.append("dadang")
print(f"menambahkan data di akhir list = {data}")

# menambahkan list
data_baru = ["ujang", "bustomi", "doni"]
data.extend(data_baru)
print(f"data gabungan = \n{data_baru}")

# merubah data 
# kita ubah dari data 2 menjadi michael
data[2]= "Michael"
print(f"mengubah data di index ke 2 = {data}")

# menghapus data
data.remove("riki")
print(f"data riki di hapus = \n{data}")

# menghapus data paling akhir
data.pop()
print(f"data paling akhir dihapus {data}")




