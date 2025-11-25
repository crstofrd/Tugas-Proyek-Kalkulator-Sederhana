def get_numbers():
  while True:
    try:
      a = float(input("Masukkan angka pertama: "))
      b = float(input("Masukkan kedua kedua: "))
      return a, b
    except ValueError:
      print("Angka tidak valid! Masukkan angka dengan benar.")
