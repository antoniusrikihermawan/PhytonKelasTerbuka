# Latian 

# Kalkulator sederhana
angka1 = int(input("Masukkan angka pertama :"))
operator = input("operator (+,-,x,):")
angka2 = int(input("Masukkan angka kedua :"))

if operator == "+":
    print(angka1 + angka2)
elif operator == "-":
    print(angka1 - angka2)
elif operator == "*":
    print(angka1 * angka2)
elif operator == ":":
    print(angka1 / angka2)
