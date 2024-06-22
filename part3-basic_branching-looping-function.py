# PART 3 - Basic Branching, Looping & Function
## Problem 1 - Konversi Nilai 
def nilai_huruf(nilai_number):
    if 80 <= nilai_number <= 100:
        return 'A'
    elif 65 <= nilai_number <= 79:
        return 'B+'
    elif 50 <= nilai_number <= 64:
        return 'B'
    elif 35 <= nilai_number <= 49:
        return 'C'
    elif 0 <= nilai_number <= 34:
        return 'D'
    else:
        return 'Nilai tidak valid'

def periksa_nilai():
    nama_mahasiswa = input("Masukkan nama mahasiswa: ")
    nilai_number = int(input("Masukkan nilai: "))
    
    nilai_huruf_mahasiswa = nilai_huruf(nilai_number)
    
    print(f"Nama Mahasiswa: {nama_mahasiswa}")
    print(f"Nilai Number: {nilai_number}")
    print(f"Nilai Huruf: {nilai_huruf_mahasiswa}")

# Memeriksa nilai mahasiswa
periksa_nilai()

## Problem - 2.1 - Faktor Bilangan
def cari_faktor(bilangan):
    faktor = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            faktor.append(i)
    return faktor

def main():
    bilangan = int(input("Masukkan sebuah bilangan: "))
    faktor = cari_faktor(bilangan)
    print(f"Faktor dari {bilangan} adalah: {faktor}")

main()

## Problem - 2.2 - Faktor Bilangan
def cari_faktor(bilangan):
    faktor = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            faktor.append(i)
    return faktor

def main():
    bilangan = int(input("Masukkan sebuah bilangan: "))
    faktor = cari_faktor(bilangan)
    print(f"Faktor dari {bilangan} adalah: {faktor}")

main()

## Problem 3 - Bilangan Prima
def is_prime(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan ** 0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

def main():
    bilangan = int(input("Masukkan sebuah bilangan: "))
    if is_prime(bilangan):
        print(f"{bilangan} adalah bilangan prima.")
    else:
        print(f"{bilangan} bukan bilangan prima.")

main()

## Problem 4 - Palindrome
def is_palindrome(kata):
    kata_bersih = kata.replace(" ", "").lower()
    return kata_bersih == kata_bersih[::-1]

def main():
    kata = input("Masukkan sebuah kata atau kalimat: ")
    if is_palindrome(kata):
        print(f"'{kata}' adalah palindrom.")
    else:
        print(f"'{kata}' bukan palindrom.")

main()

## Problem 5 - Exponentiation
def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

def main():
    x = int(input("Masukkan nilai x: "))
    n = int(input("Masukkan nilai n: "))
    hasil = power(x, n)
    print(f"{x} pangkat {n} adalah {hasil}")

main()

## Problem 6 - Full Prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_full_prime(number):
    if not is_prime(number):
        return False
    
    digits = str(number)
    for digit in digits:
        if not is_prime(int(digit)):
            return False
    return True

def main():
    number = int(input("Masukkan sebuah bilangan: "))
    if is_full_prime(number):
        print("Ya")
    else:
        print("Tidak")

main()



