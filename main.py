def main():
    while True:
        print("\n=== Kalkulator Sederhana ===")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar")

        pilihan = input("Pilih operasi (1-5): ")

        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator!")
            break

        a, b = get_numbers()

        if pilihan == '1':
            print("Hasil:", tambah(a, b))
        elif pilihan == '2':
            print("Hasil:", kurang(a, b))
        elif pilihan == '3':
            print("Hasil:", kali(a, b))
        elif pilihan == '4':
            res = bagi(a, b)
            if res is None:
                print("Error: Tidak bisa membagi dengan nol")
            else:
                print("Hasil:", res)
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
