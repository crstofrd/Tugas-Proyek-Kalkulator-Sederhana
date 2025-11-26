def get_numbers():
    while True:
        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            return a, b
        except ValueError:
            print("Angka tidak valid! Masukkan angka dengan benar.")

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return None
    return a / b

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
