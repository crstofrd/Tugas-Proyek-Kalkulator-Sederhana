#Main.py
#Akan ada fungsi import operations.py dan input_handler.py

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
