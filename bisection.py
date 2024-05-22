import numpy as np

print('='*30,'Bisection','='*30)

def fungsi(x, p, q, r, s):
   
    return p * x + q * (x ** 2) + r * (x ** 3) + s * (x ** 4)

def bisection(p, q, r, s, a, b, tol=1e-6, max_iter=100):
    
    while fungsi(a, p, q, r, s) * fungsi(b, p, q, r, s) >= 0:
        print('-'*70)
        print("\n\tKedua ujung interval memiliki tanda yang sama untuk nilai fungsi,\n\tsilakan masukkan ulang nilai A dan B.\n\t")
        print('-'*70)
        a = float(input("Masukkan nilai a (Interval): "))
        b = float(input("Masukkan nilai b (Interval): "))

    iterasi = 0
    while (b - a) / 2 > tol and iterasi < max_iter:
        c = (a + b) / 2
        if fungsi(c, p, q, r, s) == 0:
            break
        elif fungsi(c, p, q, r, s) * fungsi(a, p, q, r, s) < 0:
            b = c
        else:
            a = c
        iterasi += 1

    print('-'*70)
    print(f"\nKonvergensi diperoleh setelah {iterasi} iterasi.\n")
    print('-'*70)
    return (a + b) / 2

p = float(input("Masukkan nilai dari p: "))
q = float(input("Masukkan nilai dari q: "))
r = float(input("Masukkan nilai dari r: "))
s = float(input("Masukkan nilai dari s: "))

while True:
    a = float(input("Masukkan nilai dari a (Interval): "))
    b = float(input("Masukkan nilai dari b (Interval): "))
    
    hasil = bisection(p, q, r, s, a, b)
    if hasil is not None:
        print(f"\nPerkiraan akar: {hasil}\n")
        print('-'*70)
        break
    else:
        print("\n\tGagal menemukan akar dalam iterasi yang diberikan!!!!.\n")
