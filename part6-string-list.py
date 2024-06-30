# PART 6 - String & List
## Problem 1 - Compare String
def kata_beririsan(A, B):
    string_a = set()
    
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            string_a.add(A[i:j])
    
    string_beririsan_b = ""
    for string in string_a:
        if string in B and len(string) > len(string_beririsan_b):
            string_beririsan_b = string
    
    return string_beririsan_b

A = "KANGAROO"
B = "KANG"
print("kata yan beririsan adalah:", kata_beririsan(A, B))


## Problem 2 - Caesar Cipher
def geser_huruf(offset, string):
    hasil = ""
    for karakter in string:
        if karakter == " ":
            hasil += karakter
        else:
            kode_ascii = ord(karakter)
            kode_baru = kode_ascii + offset
            if kode_baru > 122:  # Jika melewati 'z'
                kode_baru = 97 + (kode_baru - 123) % 26
            hasil += chr(kode_baru)
    return hasil

offset = 2
string = 'alta'
print("Hasil:", geser_huruf(offset, string))


## Problem 3 - Array Unique
def array_unik(array1, array2):
    set_array2 = set(array2)
    
    result = [num for num in array1 if num not in set_array2]
    
    return result

array1 = [1, 2, 3, 4]
array2 = [1, 3, 5, 10, 16]
print("Output:", array_unik(array1, array2))


## Problem 4 - Maximum Sum Subarray of Size K
def jumlah_subarray_max(arr, k):
    max_sum = 0
    current_sum = 0

    for i in range(k):
        current_sum += arr[i]
    
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Output:", jumlah_subarray_max(arr, k))


## Problem 5 - Remove Duplicates
def remove_duplicate(arr):
    if not arr:
        return 0

    unique_index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index - 1]:
            arr[unique_index] = arr[i]
            unique_index += 1

    return unique_index

arr = [2, 3, 3, 3, 6, 9, 9]
length = remove_duplicate(arr)
print("Output:", length)
print("Array setelah menghapus duplikat:", arr[:length])



