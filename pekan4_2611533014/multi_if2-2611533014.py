#Buat nama file dengan nama multi_if2_2611533014.py
#Buat program untuk kondisional if
#Nama variabel ditambah 4 digit NIM terakhir contoh: ipk_1234
#Program ini menggunakan fungsi input ()
#Program Menghitung Diskon Belanja

# Input dan user
total_belanja_3014 = float(input("Input Total Belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y atau 't')
input_member_3014 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_3014 = input_member_3014 in ["y", "t"]

# Input satus kode promo (mengecek apakah user mengetik 'y atau 't')
input_promo_3014 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3014 = input_promo_3014 in ["y", "t"]

total_diskon_persen_3014 = 0

# Multi-if terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3014 > 1000000:
    total_diskon_persen_3014 += 10  # Diskon total besar

if is_member_3014:
    total_diskon_persen_3014 += 5  # Diskon member

if kode_promo_valid_3014:
    total_diskon_persen_3014 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3014 = total_belanja_3014 * (total_diskon_persen_3014 / 100)
total_bayar_3014 = total_belanja_3014 - nominal_diskon_3014

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_3014} (Rp {nominal_diskon_3014:.0f})")
print(f"Total Bayar   : Rp {total_bayar_3014:.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_3014}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid