# Date dan Time (latian)

import datetime as dt 
print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
print(f'Tanggal lahir anda : {tanggal_lahir}')
print(f'Hari nya adalah : {tanggal_lahir:%A}')

hari_ini = dt.date.today()
print(f'Hari ini adalah : {hari_ini}')
umur_hari= hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa  = (umur_hari.days % 365) // 30
print(umur_hari.days)
print(f'Umur anda adalah : {umur_tahun} Tahun, {umur_bulan_sisa} Bulan')

