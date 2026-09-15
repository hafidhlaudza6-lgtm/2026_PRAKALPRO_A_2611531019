# buat nama file dengan nama logika_NIM.py
# nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# program operator logika dalam Python

# Masukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1)
print("A2 =", a2)

# konjungsi: bernilai True jika keduanya True
hasil = a1 and a2
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1 or a2
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai true jika kedua nilai berbeda
hasil = a1 != a2
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)