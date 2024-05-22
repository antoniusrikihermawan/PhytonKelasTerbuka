# operator dalam bentuk method

# merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu kece ABIEzzzZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

##pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean 
print(salam + " is lower = " + str(apakah_lower) )
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <--- untuk mengecek semua huruf
alpha = "antoniusrikihermawan"
apakah_alpha = alpha.isalpha() # hasilnya boolean
print(alpha + " is alpha = " + str(apakah_alpha))

# isalnum() <--- untuk mengecek huruf dan angak
alnum = "antoniusrikihermawan545472"
apakah_alnum = alnum.isalnum() # hasilnya boolean 
print(alnum + " is alnum = " + str(apakah_alnum))

# isdecimal() <--- untuk mengecek angka saja
decimal = "123456778"
apakah_isdecimal = decimal.isdecimal() # hasilnya boolean
print(decimal + " is decimal = " + str(apakah_isdecimal))

# isspace() <--- untuk mengecek spasi, tab, newline \n
space = "    "
apakah_isspace = space.isspace() # hasilnya boolean
print(space + " is space = " + str(apakah_isspace))

# istitle() <--- semua kata dimulai dengan huruf besar
judul = "It Okay Not To Be Okay"
cek_judul = judul.istitle() # hasilnya boolean
print(judul + " is title = " + str(cek_judul))

## mengecek komponen startswith() endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") # hasilnya boolean
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Sangjangnim") # hasilnya boolean
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangkamu".split(('ehm'))
print(gabungan)

# alokasi karakter rjust(), ljust(), center()
print(5*"=" + "data" + "="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

#kebalikannya --> strip
tengah = tengah.strip("-")
print("'"+tengah+"'")





