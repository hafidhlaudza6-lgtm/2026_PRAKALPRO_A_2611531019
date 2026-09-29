# Buat file dengan nama nested_for4_nim.py
# Buat program untuk perulangan for dalam pyton
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_1019 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1019 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1019 = tinggi_1019
    c_1019 = a_1019
    lebar_1019 = (2 * tinggi_1019) - 2

    for i in range(1, tinggi_1019 + 1):
        b_1019 = c_1019 + 1

        for j in range(1, lebar_1019 + 1):

            # Baris atas dan bawah
            if i == 1 or i == tinggi_1019:
                if j == 1 or j == lebar_1019:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j == 1 or j == lebar_1019:
                    print("|", end="")
                else:
                    if j == c_1019:
                        print("<", end="")
                    elif j == b_1019:
                        print(">", end="")
                    elif j == (lebar_1019 - c_1019):
                        print("<", end="")
                    elif j == (lebar_1019 - c_1019 + 1):
                        print(">", end="")
                    elif j > b_1019 and j < (lebar_1019 - c_1019):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli java
        a_1019 -= 2

        if a_1019 <= 0:
            c_1019 = (-a_1019) + 2
        else:
            c_1019 = a_1019