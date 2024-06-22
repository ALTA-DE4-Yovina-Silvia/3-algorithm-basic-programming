# Part 2 - Variable, Data Type, Operator
## Problem 1 - Program "Hello" + "Nama"
name = "Vina"
print(f"Hello {name}!, Saya Golang, bahasa yang sangat menyenangkan.")

## Problem 2 - Menghitung Luas Segitiga
alas = 15
tinggi = 20
luas = (alas*tinggi/2)
print(luas)

alas = float(input("Masukkan alas segitiga (dalam cm): "))
tinggi = float(input("Masukkan tinggi segitiga (dalam cm): "))
luas = 0.5 * alas * tinggi
print(f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas} cm².")

## Problem 3 - Menghitung Luas Permukaan Tabung
T = float(input("Masukkan tinggi tabung (dalam cm): "))
r = float(input("Masukkan jari-jari tabung (dalam cm): "))
Pi = 3.14
luas_permukaan = 2 * Pi * r * (r + T)
print(f"Luas permukaan tabung dengan tinggi {T} cm dan jari-jari {r} cm adalah {luas_permukaan} cm².")

## Problem 4 - Program untuk menghitung harga setelah diskon
harga_awal = float(input("Masukkan harga awal (dalam satuan mata uang): "))
diskon = float(input("Masukkan persentase diskon barang: "))
harga_diskon = (diskon/100)*harga_awal
harga_akhir = harga_awal-harga_diskon
print(f"harga_diskon: {harga_diskon}")
print(f"harga_akhir setelah diskon: {harga_akhir}")

