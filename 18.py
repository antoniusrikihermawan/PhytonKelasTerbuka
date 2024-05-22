# format string

# contact generic
nama = "antonius riki hermawan"
format_str = f"hello {nama}"
print(format_str)

# angka 
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 21
format_str = f"bilangan bulat = {angka :d}"
print(format_str)

# bilangan ordo ribuan
angka = 2000000
format_str = f"bilangan jutaan = {angka :,}"
print(format_str)


# bilangan desimal
angka = 2000.34532
format_str = f"desimal = {angka :.4f}"
print(format_str)

# menampilkan landing zero 
angka = 20003.34342
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.2344
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase :.2%}"
print(format_persen)

# memformat opersi arimatika di dalam placeholder
harga = 100000
diskon = 4500
format_str = f"jumlah = {harga-diskon:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"bianry = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)

# boolean 
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)