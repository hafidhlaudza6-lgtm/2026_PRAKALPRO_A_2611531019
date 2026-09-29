n_1019 = int(input("Masukkan skala jam pasir (N): "))

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

print("#", end="")
for b_atas_1019 in range(4 * n_1019 + 5):
    print("=", end="")
print("#")

for baris_1019 in range(n_1019, 0, -1):
    print("|", end="")
    print(" ", end="")
    
    spasi_kiri_1019 = 2 * (n_1019 - baris_1019)
    for sk_1234 in range(spasi_kiri_1019):
        print(" ", end="")
        
    for angka_mundur_1019 in range(baris_1019, 0, -1):
        print(angka_mundur_1019, end="")
        if angka_mundur_1019 > 1:
            print(" ", end="")
            
    print("*", end="")
    
    print(" ", end="")
    for angka_maju_1019 in range(1, baris_1019 + 1):
        print(angka_maju_1019, end="")
        if angka_maju_1019 < baris_1019:
            print(" ", end="")
            
    spasi_kanan_1019 = 2 * (n_1019 - baris_1019)
    for skan_1234 in range(spasi_kanan_1019):
        print(" ", end="")
        
    print(" ", end="")
    print("|")

print("|", end="")
for spasi_pusat_kiri_1019 in range(2 * n_1019 + 1):
    print(" ", end="")
    
print("*", end="")

for spasi_pusat_kanan_1019 in range(2 * n_1019 + 1):
    print(" ", end="")
    
print("|")

for baris_bawah_1019 in range(1, n_1019 + 1):
    print("|", end="")
    print(" ", end="")
    
    spasi_bawah_kiri_1019 = 2 * (n_1019 - baris_bawah_1019)
    for sbk_1234 in range(spasi_bawah_kiri_1019):
        print(" ", end="")
        
    for angka_mundur_b_1019 in range(baris_bawah_1019, 0, -1):
        print(angka_mundur_b_1019, end="")
        if angka_mundur_b_1019 > 1:
            print(" ", end="")
            
    print("*", end="")
    
    print(" ", end="")
    for angka_maju_b_1019 in range(1, baris_bawah_1019 + 1):
        print(angka_maju_b_1019, end="")
        if angka_maju_b_1019 < baris_bawah_1019:
            print(" ", end="")
            
    spasi_bawah_kanan_1019 = 2 * (n_1019 - baris_bawah_1019)
    for sbkan_1019 in range(spasi_bawah_kanan_1019):
        print(" ", end="")
        
    print(" ", end="")
    print("|")

print("#", end="")
for b_bawah_1019 in range(4 * n_1019 + 5):
    print("=", end="")
print("#")