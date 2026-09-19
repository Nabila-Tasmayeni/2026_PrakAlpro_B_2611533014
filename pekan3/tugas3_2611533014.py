print("======================================")
print("       PROGRAM TRANSAKSI TOKO")
print("======================================")

# Input data pelanggan
nama_3014 = input("Nama pelanggan        : ")
status_3014 = input("Status (member/biasa) : ").lower()
harga_3014 = float(input("Harga barang          : Rp"))
jumlah_3014 = int(input("Jumlah barang         : "))
promo_3014 = input("Kode promo            : ").upper()

# Kumpulan kode promo
kode_promo_3014 = ["DISKON7", "CERIA15", "BELANJA8"]

# ==========================================
# OPERATOR ARITMATIKA
# ==========================================

total_3014 = harga_3014 * jumlah_3014
rata_rata_3014 = total_3014 / jumlah_3014

# ==========================================
# OPERATOR PERBANDINGAN
# ==========================================

cek_belanja_3014 = total_3014 >= 100000
cek_jumlah_3014 = jumlah_3014 >= 3
cek_member_3014 = status_3014 == "member"

# ==========================================
# OPERATOR KEANGGOTAAN
# ==========================================

cek_promo_3014 = promo_3014 in kode_promo_3014

# ==========================================
# OPERATOR LOGIKA
# ==========================================

dapat_diskon_3014 = cek_member_3014 and cek_belanja_3014
dapat_promo_3014 = cek_promo_3014 and cek_jumlah_3014
akses_toko_3014 = cek_member_3014 or cek_belanja_3014
bukan_member_3014 = not cek_member_3014

# Menghitung diskon
if dapat_diskon_3014:
    diskon_3014 = total_3014 * 10 / 100
else:
    diskon_3014 = 0

total_bayar_3014 = total_3014 - diskon_3014

# ==========================================
# OPERATOR PENUGASAN
# ==========================================

poin_3014 = 0
poin_3014 += jumlah_3014

# ==========================================
# OPERATOR IDENTITAS
# ==========================================

promo_utama_3014 = kode_promo_3014
promo_salinan_3014 = kode_promo_3014.copy()

cek_identitas_3014 = promo_utama_3014 is kode_promo_3014
cek_beda_3014 = promo_utama_3014 is not promo_salinan_3014

# ==========================================
# OPERATOR BITWISE
# ==========================================

kode_akses_3014 = 0

# 0001 = member
if cek_member_3014:
    kode_akses_3014 |= 1

# 0010 = belanja minimal
if cek_belanja_3014:
    kode_akses_3014 |= 2

# 0100 = jumlah barang cukup
if cek_jumlah_3014:
    kode_akses_3014 |= 4

# 1000 = promo tersedia
if cek_promo_3014:
    kode_akses_3014 |= 8

# AND
cek_member_bit_3014 = kode_akses_3014 & 1
cek_promo_bit_3014 = kode_akses_3014 & 8

# XOR
kode_referensi_3014 = 9
hasil_xor_3014 = kode_akses_3014 ^ kode_referensi_3014

# Shift kiri
hasil_shift_3014 = kode_akses_3014 << 1

# ==========================================
# HASIL PROGRAM
# ==========================================

print("\n======================================")
print("          DATA TRANSAKSI")
print("======================================")

print("Nama pelanggan   :", nama_3014)
print("Status pelanggan :", status_3014)
print("Harga barang     : Rp", harga_3014)
print("Jumlah barang    :", jumlah_3014)
print("Kode promo       :", promo_3014)

print("\n------------ VALIDASI ------------")
print("Belanja >= 100000 :", cek_belanja_3014)
print("Jumlah >= 3       :", cek_jumlah_3014)
print("Status member     :", cek_member_3014)
print("Promo tersedia    :", cek_promo_3014)
print("Dapat diskon      :", dapat_diskon_3014)
print("Dapat promo       :", dapat_promo_3014)

print("\n---------- PERHITUNGAN ----------")
print("Total belanja     : Rp", total_3014)
print("Diskon            : Rp", diskon_3014)
print("Total pembayaran  : Rp", total_bayar_3014)
print("Rata-rata harga   : Rp", rata_rata_3014)

print("\n--------- HAK AKSES ---------")
print("Akses toko        :", akses_toko_3014)
print("Bukan member      :", bukan_member_3014)
print("Poin pelanggan    :", poin_3014)

print("\n--------- IDENTITAS ---------")
print("Identitas sama    :", cek_identitas_3014)
print("Identitas berbeda :", cek_beda_3014)

print("\n--------- BITWISE ---------")
print("Kode biner        :", format(kode_akses_3014, "04b"))
print("Kode desimal      :", kode_akses_3014)

print("\nCek member")
print(format(kode_akses_3014, "04b"), "& 0001")
print("Hasil             :", format(cek_member_bit_3014, "04b"))
print("Desimal           :", cek_member_bit_3014)

print("\nCek promo")
print(format(kode_akses_3014, "04b"), "& 1000")
print("Hasil             :", format(cek_promo_bit_3014, "04b"))
print("Desimal           :", cek_promo_bit_3014)

print("\nXOR")
print(format(kode_akses_3014, "04b"), "^", format(kode_referensi_3014, "04b"))
print("Hasil             :", format(hasil_xor_3014, "04b"))
print("Desimal           :", hasil_xor_3014)

print("\nSHIFT LEFT")
print(format(kode_akses_3014, "04b"), "<< 1")
print("Hasil             :", format(hasil_shift_3014, "04b"))
print("Desimal           :", hasil_shift_3014)

print("\n======================================")
print("             SELESAI")
print("======================================")