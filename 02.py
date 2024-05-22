def main():
    print("Selamat datang di Program Kegiatan Sehari-hari!")

    while True:
        print("\nPilih kegiatan:")
        print("1. Hitung luas persegi panjang")
        print("2. Cek status cuaca")
        print("3. Hitung biaya belanja")
        print("4. Keluar")

        choice = input("Masukkan pilihan (1-4): ")

        if choice == '1':
            hitung_luas_persegi_panjang()
        elif choice == '2':
            cek_status_cuaca()
        elif choice == '3':
            hitung_biaya_belanja()
        elif choice == '4':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    print(f"Luas persegi panjang: {luas}")


def cek_status_cuaca():
    cuaca = input("Masukkan status cuaca (cerah/hujan/berawan): ").lower()

    if cuaca == "cerah":
        print("Cuaca cerah, ideal untuk aktivitas luar ruangan.")
    elif cuaca == "hujan":
        print("Cuaca hujan, sebaiknya persiapkan payung atau jas hujan.")
    elif cuaca == "berawan":
        print("Cuaca berawan, tetap waspada terhadap perubahan cuaca.")
    else:
        print("Status cuaca tidak dikenali.")


def hitung_biaya_belanja():
    total_biaya = 0

    while True:
        nama_barang = input("Masukkan nama barang (selesai untuk mengakhiri): ")
        if nama_barang.lower() == "selesai":
            break
        else:
            harga_barang = float(input("Masukkan harga barang: "))
            jumlah_barang = int(input("Masukkan jumlah barang: "))
            total_biaya += harga_barang * jumlah_barang

    print(f"Total biaya belanja: {total_biaya}")


if __name__ == "__main__":
    main()
