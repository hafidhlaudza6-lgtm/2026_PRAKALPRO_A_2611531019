# Buat file dengan nama nested_for3_nim.py
# Buat program untuk perulangan for dalam pyton
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1019 = int(input("Masukkan nilai batas: "))
for i in range(batas_1019+1):
    for j in range(batas_1019+1):
        print(i+j, end=" ")
    print() # pindah ke baris berikutnya