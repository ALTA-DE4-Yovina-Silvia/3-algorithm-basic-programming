# PART 5 - Complexity Analysis
## Problem 1 - Bilangan Prima
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Masukkan bilangan: "))
if is_prime(number):
    print(f"{number} adalah bilangan prima.")
else:
    print(f"{number} bukan bilangan prima.")


## Problem 2 - Fast Exponentiation
def pow(a, b):
    return a**b
    
print(pow(2, 3))
print(pow(7, 2))
print(pow(10, 5))
print(pow(17, 6))
print(pow(5, 3))


## Problem 3 - Join Array Remove Duplicate
def gabungkan_list(list1, list2):
    gabungan_dict = {}
    for nama in list1:
        gabungan_dict[nama] = True

    for nama in list2:
        gabungan_dict[nama] = True
    
    return list(gabungan_dict.keys())

list1 = ["Adam", "Budi", "Eva"]
list2 = ["Budi", "David", "Eva"]

hasil = gabungkan_list(list1, list2)
print(hasil)


## Problem 4 - Angka Muncul Sekali
def angka_unik(list_angka):
    frekuensi = {}
    for angka in list_angka:
        if angka in frekuensi:
            frekuensi[angka] += 1
        else:
            frekuensi[angka] = 1
    
    hasil = [int(angka) for angka in frekuensi if frekuensi[angka] == 1]
    return hasil

list_angka = input("Masukkan list angka: ")
output = angka_unik(list_angka)
print(output)


## Problem 5 - Pair with Target Sum
def pasangan_dengan_target(arr, target):
    kiri = 0  
    kanan = len(arr) - 1  
    
    while kiri < kanan:
        jumlah = arr[kiri] + arr[kanan]
        if jumlah == target:
            return [kiri, kanan]
        elif jumlah < target:
            kiri += 1
        else:
            kanan -= 1
            
    return []

array1 = [1, 2, 3, 4, 6]
target1 = 6
output1 = pasangan_dengan_target(array1, target1)
print(f"Output untuk array berurutan: {output1}")  # Output: [1, 3]

array2 = [2, 5, 9, 11]
target2 = 11
output2 = pasangan_dengan_target(array2, target2)
print(f"Output untuk array berurutan: {output2}")  # Output: [0, 2]