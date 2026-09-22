print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_pengunjung_1019 = input("Masukkan Nama Pengunjung : ")
umur_1019 = int(input("Input umur anda          : "))
sim_1019 = input("Apakah Anda Sudah Punya SIM C (y/t) : ").lower()

print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

nomor_paket_1019 = int(input("Masukkan nomor paket (1-5)     : "))
jumlah_tiket_1019 = int(input("Masukkan jumlah tiket          : "))
member_1019 = input("Apakah Anda member? (y/t)      : ").lower()
promo_1019 = input("Apakah kode promo valid? (y/t) : ").lower()


match nomor_paket_1019:
    case 1:
        nama_paket_1019 = "Safari Rimba"
        harga_satuan_1019 = 50000
    case 2:
        nama_paket_1019 = "Arung Jeram"
        harga_satuan_1019 = 75000
    case 3:
        nama_paket_1019 = "Motor ATV Ekstrim"
        harga_satuan_1019 = 120000
    case 4:
        nama_paket_1019 = "Roller Coaster Kilat"
        harga_satuan_1019 = 100000
    case 5:
        nama_paket_1019 = "All-Access VIP"
        harga_satuan_1019 = 220000
    case _:
        nama_paket_1019 = "Tidak Valid"
        harga_satuan_1019 = 0

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if nomor_paket_1019 == 3:
    if umur_1019 >= 17 and (sim_1019 == "y" or sim_1019 == "ya"):
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_1019 >= 17 and sim_1019!= "y" :
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)")
    elif umur_1019 < 17 and sim_1019 == "y" :
        print("Identitas tidak valid: Belum cukup umur memiliki SIM")
    else:
        print("Status Akses: Maaf, Anda belum memenuhi syarat umur/SIM untuk ATV.")
else:
    if nomor_paket_1019 != 3:
     if umur_1019 <= 5:
        print(f"Status Akses: Pengunjung balita, wajib didampingi orang tua di {nama_paket_1019}.")
     elif umur_1019 >= 60:
        print(f"Status Akses: Pengunjung senior, mendapatkan jalur khusus di {nama_paket_1019}.")
     else:
        print(f"Status Akses: Silahkan menikmati wahana {nama_paket_1019}.")


subtotal_1019 = harga_satuan_1019 * jumlah_tiket_1019
persen_diskon_1019 = 0

if subtotal_1019 >= 200000 :
    persen_diskon_1019 += 10  # Diskon belanja besar
if member_1019 == "y" or member_1019 == "ya":
    persen_diskon_1019 += 20  # Tambahan diskon member 20%
if promo_1019 == "y" or promo_1019 == "ya":
    persen_diskon_1019 += 10  # Tambahan diskon promo 10%
if persen_diskon_1019 > 50:
    persen_diskon_1019 = 50

total_diskon_1019 = int(subtotal_1019 * (persen_diskon_1019 / 100))
total_bayar_1019 = subtotal_1019 - total_diskon_1019

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_1019:,}")
if subtotal_1019 > 300000:
    print("Selamat! Anda berhak mendapatkan Souvenir gratis")
print(f"Total Diskon     : {persen_diskon_1019}% (Rp {int(total_diskon_1019):,})")
print(f"Total Bayar      : Rp {int(total_bayar_1019):,}")
print("Catatan Layanan  : Terima kasih telah berkunjung.")
print("Program Selesai")