# buat file dengan nama aritmatika_NIM.py
# buat program untuk operator aritmatika dalam Python
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1019 = int(input("Input angka-1: "))
angka2_1019 = int(input("Input angka-2: "))

# penjumlahan
hasil = angka1_1019 + angka2_1019
print("/nOperator Penjumlahan")
print("Hasil =", hasil)

# pengurangan
hasil = angka1_1019 - angka2_1019
print("/nOperator Pengurangan")
print("Hasil =", hasil)

# perkalian
hasil = angka1_1019 * angka2_1019
print("/nOperator Perkalian")
print("Hasil =", hasil)

# pembagian, pembagian bulat, dan sisa bagi
if angka2_1019 != 0:
    hasil = angka1_1019 / angka2_1019
    print("/nOperator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1_1019 // angka2_1019
    print("/nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_1019 % angka2_1019
    print("/nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0")

# pangkat
hasil = angka1_1019 ** angka2_1019
print("/nOperator Pangkat")
print("Hasil =", hasil)