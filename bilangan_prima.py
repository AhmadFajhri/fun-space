#Rumus bilangan prima
def is_prime(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
  elif n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

angka = int(input("Masukkan angka: "))

if is_prime(angka):
  print(angka, "adalah bilangan prima")
else:
  print(angka, "bukan bilangan prima")


# Menghitung luas persegi panjang
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Input panjang dan lebar dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Memanggil fungsi untuk menghitung luas
luas_persegi_panjang = hitung_luas_persegi_panjang(panjang, lebar)

# Menampilkan hasil
print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas_persegi_panjang}")
