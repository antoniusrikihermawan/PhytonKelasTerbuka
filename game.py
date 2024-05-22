import random

welcome_message = "WELCOME TO GAMES!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama = input("masukka nama anda : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 10# INI HARUS TETAP KOSONG

goa = goa_kosong.copy() #INI ADALAH TEMPAT BARU CUPY


goa[cuypy_position -1] = "|0_0|"
print(f"posisi : {cuypy_position} ")

print(f'''Halo {nama}! Coba perhatikan goa dibawah ini
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu goa nomor berapa CUYPY berada ? [1 / 2 / 3 / 4] : "))
confirm_answer = input(f"Apakah kamu yakin dengan jawabanmu {pilihan_user} [y / n] : ")

if confirm_answer == "n":
    print("Program dihentikan!")
    exit()
elif confirm_answer == "y" :
    if pilihan_user == cuypy_position :
        print(f"Selamat {goa} Selamat kamu menang! posisi CUYPY ada di goa nomor {cuypy_position}")
    else :
        print(f"{goa}, KAMU KALAH! cuypy bukan berada disitu, tapi di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}")
else :
    print("Silahkan ulangi programnya!")
    exit()




