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

    for i_1019 in range(1, tinggi_1019 + 1):
        b_1019 = c_1019 + 1

        for j_1019 in range(1, lebar_1019 + 1):

            # Baris atas dan bawah
            if i_1019 == 1 or i_1019 == tinggi_1019:
                if j_1019 == 1 or j_1019 == lebar_1019:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_1019 == 1 or j_1019 == lebar_1019:
                    print("|", end="")
                else:
                    if j_1019 == c_1019:
                        print("<", end="")
                    elif j_1019 == b_1019:
                        print(">", end="")
                    elif j_1019 == (lebar_1019 - c_1019):
                        print("<", end="")
                    elif j_1019 == (lebar_1019 - c_1019 + 1):
                        print(">", end="")
                    elif j_1019 > b_1019 and j_1019 < (lebar_1019 - c_1019):
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