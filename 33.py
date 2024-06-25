data_1 = [1,2,3,4,5,6,7,8,9,10]
data_2 = [11,12,13,14,15,16,17,18,19]

data_list_biasa = [1,2,3,4,5,6,7,8]
print(f"data list biasa = {data_list_biasa}")

list_2d = [data_1, data_2]
print(f"list_2d = {list_2d}")

# contoh penggunaan 
peserta_1 = ["ucup",25,"laki-laki"]
peserta_2 = ["otong",10,"laki-laki"]
peserta_3 = ["deden",15,"laki-laki"]

list_peserta = [peserta_1,peserta_2,peserta_3]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
     print(f"nama\t= {peserta[0]}")
     print(f"umur\t= {peserta[1]}")
     print(f"jenis kelamin\t= {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")
peserta_1[0] = "Michael"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")
