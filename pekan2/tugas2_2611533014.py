from typing import Final

BATAS_3014: Final[float] = 75.0

print("=== DATA PRAKTIKAN ===")

nama_3014 = input("Nama           : ")
nim_3014 = int(input("NIM            : "))
umur_3014 = int(input("Umur           : "))
jenis_3014 = input("Jenis Kelamin   : ")
semester_3014 = int(input("Semester       : "))
nilai_3014 = float(input("Nilai Praktikum: "))
alamat_3014 = input("Alamat         : ")

# Data complex
kode_3014 = complex(nim_3014, semester_3014)

# Cek kelulusan
lulus_3014 = nilai_3014 >= BATAS_3014

print("\n=== HASIL DATA ===")
print("Nama     :", nama_3014, "|", type(nama_3014))
print("NIM      :", nim_3014, "|", type(nim_3014))
print("Umur     :", umur_3014, "|", type(umur_3014))
print("Jenis Kelamin :", jenis_3014, "|", type(jenis_3014))
print("Semester :", semester_3014, "|", type(semester_3014))
print("Nilai    :", nilai_3014, "|", type(nilai_3014))
print("Alamat   :", alamat_3014, "|", type(alamat_3014))
print("Kode     :", kode_3014, "|", type(kode_3014))

print("\n=== STATUS KELULUSAN ===")
print("Batas Nilai :", BATAS_3014)
print("Lulus       :", lulus_3014, "|", type(lulus_3014))

if lulus_3014:
    print("Keterangan  : LULUS")
else:
    print("Keterangan  : TIDAK LULUS")
