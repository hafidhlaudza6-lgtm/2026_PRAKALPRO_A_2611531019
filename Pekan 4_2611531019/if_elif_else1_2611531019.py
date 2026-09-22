# Buat file dengan nama if_elif_else_nim.py
# Buat program untuk kondisonal if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
#Program ini menggunakan fungsi input()

umur_1019 = int(input("Input Umur Anda"))
sim_1019 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_1019 >= 17 and sim_1019 == 'y':
    print("Anda Sudah Dewasa dan boleh bawa motor")
elif umur_1019 >= 17 and sim_1019 != 'y':
    print("Anda Sudah Dewasa tetapi tidak boleh bawa motor")
elif umur_1019 < 17 and sim_1019 == 'y':
        print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur Bawa Motor")
print("Program Selesai")