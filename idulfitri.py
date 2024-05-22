import numpy as np

print('='*30,'Bisection','='*30)

def fungsi(x):
    return x**4 - 3*x**3 - 2*x**2 + 8*x - 4

def bisection(a, b, tol=1e-6, max_iter=100):
    while fungsi(a) * fungsi(b) >= 0:
        print('-'*70)
        print("\n\tKedua ujung interval memiliki tanda yang sama untuk nilai fungsi,\n\tsilakan masukkan ulang nilai a dan b.\n\t")
        print('-'*70)
        a = float(input("Masukkan nilai a (Interval): "))
        b = float(input("Masukkan nilai b (Interval): "))
        # Tambahkan kondisi untuk menghentikan loop jika a dan b sudah valid
        if fungsi(a) * fungsi(b) < 0:
            break

    iterasi = 0
    while (b - a) / 2 > tol and iterasi < max_iter:
        c = (a + b) / 2
        print(f"Iterasi {iterasi + 1}: a = {a}, b = {b}, c = {c}, f(c) = {fungsi(c)}")
        if fungsi(c) == 0:
            break
        elif fungsi(c) * fungsi(a) < 0:
            b = c
        else:
            a = c
        iterasi += 1

    print('-'*70)
    if iterasi >= max_iter:
        print("\n\tMetode tidak konvergen setelah jumlah iterasi maksimum yang ditentukan.\n")
        print('-'*70)
        return None
    else:
        print(f"\nKonvergensi diperoleh setelah {iterasi} iterasi.\n")
        print('-'*70)
        return (a + b) / 2

a = 0
b = 2

hasil = bisection(a, b)
if hasil is not None:
    print(f"\nPerkiraan akar: {hasil}\n")
    print('-'*70)
