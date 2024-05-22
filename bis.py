def f(p, q, r, s, x):
    return p * x**3 + q * x**2 + r * x + s

def bisection(p, q, r, s, a, b, tolerance=1e-5, max_iterations=100):
    if f(p, q, r, s, a) * f(p, q, r, s, b) > 0:
        print("Interval tidak valid, fungsi memiliki nilai yang sama di kedua ujung interval.")
        return None
    
    iteration = 0
    while iteration < max_iterations:
        c = (a + b) / 2.0
        if abs(f(p, q, r, s, c)) < tolerance:
            return c
        
        if f(p, q, r, s, c) * f(p, q, r, s, a) < 0:
            b = c
        else:
            a = c
        
        iteration += 1
    
    print("Iterasi maksimum telah tercapai.")
    return None

# Input koefisien fungsi dan batas interval
p = float(input("Masukkan koefisien p: "))
q = float(input("Masukkan koefisien q: "))
r = float(input("Masukkan koefisien r: "))
s = float(input("Masukkan koefisien s: "))
a = float(input("Masukkan batas awal interval (a): "))
b = float(input("Masukkan batas akhir interval (b): "))

# Panggil fungsi bisection dan cetak hasil
root = bisection(p, q, r, s, a, b)
if root is not None:
    print("Akar: {:.5f}".format(root))
else:
    print("Tidak dapat menemukan akar dalam interval yang diberikan.")
