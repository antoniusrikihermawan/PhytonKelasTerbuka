# looping dari list

# for loop 
print("Looping dari list")
kumpulan_angka = [4,3,2,5,6,1]

for i in kumpulan_angka:
     print(f"angka = {i}")

peserta = ["ucup", "otong", "dadang", "diding"]

for i in peserta:
     print(f"nama = {i}")

#for loop dan range
print("\n for loop dan range")
kumpulan_angka = [10,3,5,6,7]

panjang = len(kumpulan_angka)

for i in range(panjang):
     print(f"angka = {kumpulan_angka[i]}")

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
     print(f"angka = {kumpulan_angka[i]}")
     i += 1

# list comprehension
data = ["ucup",1,2,3, "otong"]
[print(f"data={i}") for i in data]

angka = [10,11,12,13,14]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print(f"Enumerate")
data_list = ["ucup",1,2,3, "otong"]

for index, data in enumerate(data_list):
     print(f"index = {index}, data = {data}")