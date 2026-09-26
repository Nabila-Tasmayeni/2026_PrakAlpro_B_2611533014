print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input data pengunjung
nama_3014 = input("Masukkan Nama Pengunjung : ")
umur_3014 = int(input("Input umur anda : "))
sim_3014 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()
jumlah_tiket_3014 = int(input("Masukkan jumlah tiket : "))

# Validasi jumlah tiket
if jumlah_tiket_3014 <= 0:
    print("Peringatan: Jumlah tiket tidak valid!")

# Pilihan wahana
print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

paket_3014 = int(input("Masukkan nomor paket (1-5): "))

# Menentukan wahana dan harga
match paket_3014:
    case 1:
        nama_wahana_3014 = "Wahana Safari Rimba"
        harga_satuan_3014 = 50000
    case 2:
        nama_wahana_3014 = "Wahana Arung Jeram"
        harga_satuan_3014 = 75000
    case 3:
        nama_wahana_3014 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3014 = 120000
    case 4:
        nama_wahana_3014 = "Wahana Roller Coaster Kilat"
        harga_satuan_3014 = 100000
    case 5:
        nama_wahana_3014 = "Wahana All-Access VIP"
        harga_satuan_3014 = 220000
    case _:
        print("Paket wahana tidak valid!")
        raise SystemExit

# Input member dan promo
is_member_3014 = input("Apakah Anda member? (y/t): ").strip().lower()
kode_promo_valid_3014 = input("Apakah kode promo valid? (y/t): ").strip().lower()

# Validasi izin wahana
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3014 == 3:
    if umur_3014 >= 17 and sim_3014 == "y":
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_3014 >= 17 and sim_3014 != "y":
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_3014 < 17 and sim_3014 == "y":
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_3014 >= 10:
        print("Status Akses: Anda memenuhi batas umur wahana.")
    else:
        print("Status Akses: Anda belum cukup umur untuk wahana ini.")

# Menghitung subtotal
subtotal_3014 = harga_satuan_3014 * jumlah_tiket_3014

# Menghitung diskon
total_diskon_persen_3014 = 0

if subtotal_3014 >= 200000:
    total_diskon_persen_3014 += 10

if is_member_3014 in ["y", "ya"]:
    total_diskon_persen_3014 += 5

if kode_promo_valid_3014 in ["y", "ya"]:
    total_diskon_persen_3014 += 15

if jumlah_tiket_3014 >= 5:
    total_diskon_persen_3014 += 5

# Menghitung pembayaran
nominal_diskon_3014 = subtotal_3014 * (total_diskon_persen_3014 / 100)
total_bayar_3014 = subtotal_3014 - nominal_diskon_3014

# Menampilkan rincian pembayaran
print("\n--- RINCIAN PEMBAYARAN ---")
print("Nama Pengunjung : ", nama_3014)
print("Wahana          : ", nama_wahana_3014)
print(f"Subtotal Belanja : Rp {subtotal_3014:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3014}% (Rp {nominal_diskon_3014:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3014:,.0f}")

# Evaluasi total bayar
if total_bayar_3014 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")

print("Program Selesai")