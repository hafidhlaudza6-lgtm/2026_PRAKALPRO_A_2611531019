# Buat file dengan nama nested_for3_nim.py
# Buat program untuk perulangan for dalam pyton
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1019 = int(input("Masukkan nilai batas: "))
for i_1019 in range(batas_1019 + 1):
    for j_1019 in range(batas_1019 + 1):
        print(i_1019 + j_1019, end=" ")
    print() # pindah ke baris berikutnya