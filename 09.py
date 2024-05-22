
print("\nPROGRAM KONVERSI SUHU\n")
celcius = float(input("masukkan suhu dalam celcius : "))
print("suhu adalah : ",celcius, "celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur, "reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelviin adalah",kelvin, "kelvin")

#fahrenheit ke kelvin
fahrenheit = float(input("masukkan data :",))
celcius = 5/9 * (fahrenheit-32)
kelvin = celcius + 273
print("suhu adalah",kelvin, "kelvin")

#kelvin ke fahrenheit
kelvin = float(input("masukkan data :",))
celcius = kelvin - 273
fahrenheit = (9/5 * celcius) + 32
print("suhu adalah :",fahrenheit, "fahrenheit")
