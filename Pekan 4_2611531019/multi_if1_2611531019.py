# Buat file dengan nama multi_if1.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_1019 = int(input("Input Umur Anda"))
sim_1019 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_1019 >= 17 and sim_1019 == 'y':
    print("Anda Sudah Dewasa dan boleh bawa motor")

if umur_1019 >= 17 and sim_1019 == 't':
    print("Anda Sudah Dewasa tetapi tidak boleh bawa motor")

if umur_1019 < 17 and sim_1019 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_1019 < 17 and sim_1019 == 'y':
    print("Anda Belum Cukup Umur Bawa Motor")