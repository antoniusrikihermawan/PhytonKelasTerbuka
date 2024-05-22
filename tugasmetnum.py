
import math

# Fungsi untuk mengubah sudut dari derajat ke radian
def derajat_ke_radian(derajat):
    return derajat * math.pi / 180

# Fungsi untuk menghitung perkiraan nilai kosinus menggunakan deret Taylor
def deret_taylor_cos(x, n):
    perkiraan_cos = 0

    for i in range(n):
        koefisien = (-1) ** i
        pangkat = x ** (2*i)
        faktorial = math.factorial(2*i)
        perkiraan_cos += (koefisien * pangkat) / faktorial
    return perkiraan_cos

# Input nilai sudut dari pengguna dalam bentuk derajat
x = float(input("Masukkan nilai dalam bentuk derajat: "))
sudut_radian = derajat_ke_radian(x)

# Input jumlah suku deret Taylor
xo = int(input("Masukkan jumlah suku deret Taylor: "))

# Hitung perkiraan nilai kosinus menggunakan deret Taylor
perkiraan_cos = deret_taylor_cos(sudut_radian, xo)

# Tampilkan hasil perkiraan nilai kosinus
print("Hasil perkiraan kosinus dengan deret Taylor:", perkiraan_cos)
