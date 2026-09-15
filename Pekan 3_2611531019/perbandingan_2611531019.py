# buat nama file dengan nama perbandingan_NIM.py
# nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator perbandingan dalam Python

angka1_1019 = int(input("Input angka-1: "))
angka2_1019 = int(input("Input angka-2: "))

# Lebih besar dari
hasil = angka1_1019 > angka2_1019
print("/nOperator lebih besar dari")
print("angka1_1019 > angka2_1019 =", hasil)

# Lebih kecil dari
hasil = angka1_1019 < angka2_1019
print("/nOperator lebih kecil dari")
print("angka1_1019 < angka2_1019 =", hasil)

# Lebih besar dari atau sama dengan
hasil = angka1_1019 >= angka2_1019
print("/nOperator lebih besar dari atau sama dengan")
print("angka1_1019 >= angka2_1019 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_1019 <= angka2_1019
print("/nOperator lebih kecil dari atau sama dengan")
print("angka1_1019 <= angka2_1019 =", hasil)

# Sama dengan
hasil = angka1_1019 == angka2_1019
print("/nOperator sama dengan")
print("angka1_1019 == angka2_1019 =", hasil)

# Tidak sama dengan
hasil = angka1_1019 != angka2_1019
print("/nOperator tidak sama dengan")
print("angka1_1019 != angka2_1019 =", hasil)

# Tambahan: perbandingan berantai dalam Python
hasil = 0 < angka1_1019 < 100
print("/nPerbandingan berantai")
print("0 < angka1_1019 < 100 =", hasil)

hasil = 0 < angka2_1019 < 100
print("0 < angka2_1019 < 100 =", hasil)