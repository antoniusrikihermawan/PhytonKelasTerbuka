# -----LIST-----

# kumpulan data numbers
data_angka = [1,2,3,4,5,6,7,8,9]
print(data_angka)

# kumpulan data string
data_string = ["riki","widodo","aris"]
print(data_string)

# kumpulan data boolean
data_boolean = [True,False,True,True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"sempol",2,"cilok","widodo","aris"]
print(data_campuran)

# cara alternatif membuaut list
data_range = range(0,10)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comperhension
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for pakek if
list_pake_for_if = [i for i in range (0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range (0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range (0,10) if i%2 != 0]
print(list_pake_for_if)