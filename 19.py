# Width and Multiline

# Data 

data_nama = 'Antonius Riki Hermawan'
data_umur = 21
data_tinggi = 157.1
data_nomor_sepatu = 42

# String Standart
data_string = f"Nama : {data_nama}, Umur : {data_umur}, Tinggi : {data_tinggi}, Nomor Sepatu : {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String Multiline (dengan menggunakan enter, newLine, \n)
data_string = f"Nama : {data_nama}\nUmur : {data_umur}\nTinggi : {data_tinggi}\nNomor Sepatu : {data_nomor_sepatu}"
print(5*"="+"Data String Multiline"+5*"=")
print(data_string)

# String Multiline (kutip triplets)
data_string = f"""
nama = {data_nama:>10}
umur = {data_umur:>10}
tinggi = {data_tinggi:>10}
data_nomor_sepatu = {data_nomor_sepatu:>10}
"""
print(5*"="+"Data String Multiline"+5*"=")
print(data_string)


