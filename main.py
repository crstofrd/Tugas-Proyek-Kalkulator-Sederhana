#Main.py
import operations
import input_handler

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

        a, b = input_handler.get_numbers()

        if pilihan == '1':
            print("Hasil:", operations.tambah(a, b))
        elif pilihan == '2':
            print("Hasil:", operations.kurang(a, b))
        elif pilihan == '3':
            print("Hasil:", operations.kali(a, b))
        elif pilihan == '4':
            print("Hasil:", operations.bagi(a, b))
        else:
            print("Pilihan tidak valid!")

#operation.py

def tambah(a, b): return a + b

def kurang(a, b): return a - b

def kali(a, b): return a * b

def bagi(a,b): if b == 0:

return "Error: Tidak bisa membagi dengan nol"

return a/b 

if __name__ == "_main_": 
    main()


