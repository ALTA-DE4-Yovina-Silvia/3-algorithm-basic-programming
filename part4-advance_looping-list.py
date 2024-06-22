# PART 4 - ADVANCE LOOPING & LIST
## Problem 1 - Play With Asterisk
def print_triangle(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')

        for k in range(i + 1):
            print('*', end=' ')
        
        print()

n = int(input("Masukkan jumlah baris: "))

print_triangle(n)

## Problem 2 - Draw XYZ
def drawXYZ(N):
    result = ""
    for row in range(N):
        for col in range(1, N + 1):
            index = row * N + col
            if index % 3 == 0:
                result += "X "
            elif index % 2 == 0:
                result += "Z "
            else:
                result += "Y "
        result += "\n"  
    
    print(result)

N = int(input("Masukkan nilai N: "))

drawXYZ(N)

## Problem 3 - Cetak Tabel Perkalian
def print_multiplication_table(n):
    if n < 1 or n > 30:
        print("Masukkan bilangan antara 1 hingga 30.")
        return
    
    print("    ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (4 * (n + 1)))

    for i in range(1, n + 1):
        print(f"{i:2} |", end="")
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()

n = int(input("Masukkan nilai n (1-30): "))

print_multiplication_table(n)

## Problem 4 - Ubah Huruf
def create_shifted_alphabet(shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return shifted_alphabet

def encrypt_message(message, shifted_alphabet):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_message = ""

    for char in message:
        if char.upper() in alphabet:
            index = alphabet.index(char.upper())
            encrypted_char = shifted_alphabet[index]
            if char.islower():
                encrypted_message += encrypted_char.lower()
            else:
                encrypted_message += encrypted_char
        else:
            encrypted_message += char

    return encrypted_message

def main():
    shift = 10
    shifted_alphabet = create_shifted_alphabet(shift)

    print("Alfabet asli:       ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(f"Alfabet Bob:       {shifted_alphabet}")

    message = input("Masukkan pesan untuk dienkripsi: ")

    encrypted_message = encrypt_message(message, shifted_alphabet)
    print(f"Pesan terenkripsi: {encrypted_message}")

main()

## Problem 5 - Mean dan Median
def calculate_mean(numbers):
    mean_value = sum(numbers) / len(numbers)
    return round(mean_value)

def calculate_median(numbers):
    n = len(numbers)
    if n % 2 == 1:
        median_value = numbers[n // 2]
    else:
        mid1 = n // 2
        mid2 = mid1 - 1
        median_value = (numbers[mid1] + numbers[mid2]) / 2
    return median_value

def main():
    numbers = list(map(int, input("Masukkan angka-angka terurut, dipisahkan dengan spasi: ").split()))
    
    mean_value = calculate_mean(numbers)
    median_value = calculate_median(numbers)
    
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")

main()
