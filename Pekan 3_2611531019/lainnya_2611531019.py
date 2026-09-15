# Buat file dengan nama lainnya_NIM.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan nilai yang ingin dicari: "))

# Operator in
hasil_1019 = nilai_dicari in data
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data,"=", hasil_1019)

# Operator not in
hasil_1019 = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data,"=", hasil_1019)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_1019 = data

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1019 = objek1_1019

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1019 = data.copy()

print("objek1_1019 =", objek1_1019)
print("objek2_1019 =", objek2_1019)
print("objek3_1019 =", objek3_1019)

# Operator is
hasil_1019 = objek1_1019 is objek2_1019
print("\nOperator identitas IS")
print("objek1_1019 is objek2_1019 =", hasil_1019)

# Operator is not
hasil_1019 = objek1_1019 is not objek3_1019
print("\nOperator identitas IS NOT")
print("objek1_1019 is not objek3_1019 =", hasil_1019)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_1019 is objek3_1019:", objek1_1019 is objek3_1019)
print("objek1_1019 == objek3_1019:", objek1_1019 == objek3_1019)