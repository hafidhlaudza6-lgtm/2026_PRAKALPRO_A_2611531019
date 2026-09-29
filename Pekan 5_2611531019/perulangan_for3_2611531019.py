# Buat file dengan nama perulangan_for2_nim.py
# Buat program untuk perulangan for dalam pyton
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1019 = int(input("Masukkan jumlah perulangan: "))

jumlah_1019 = 0
for i_1019 in range(1, ulang_1019 + 1):
    print(i_1019, end=" ")
    jumlah_1019 = jumlah_1019 + i_1019

    if i_1019 < ulang_1019:
        print(" + ", end="")
    else:
        print(" = ", jumlah_1019, end="")
print()
print("Jumlah =", jumlah_1019)