#buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: Jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_1019 = float(input('Masukkan jari-jari: '))
luas_1019 = PI * jari_1019 * jari_1019
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1019, luas_1019))