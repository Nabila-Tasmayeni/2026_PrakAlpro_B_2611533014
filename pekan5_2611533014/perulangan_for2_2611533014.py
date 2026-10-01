#Buat file dengan nama perulangan_for2_2611533014.py
#Buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit NIM terakhir contoh:ulang_1234
#Program ini menggunakan fungsi input ()

ulang_3014 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_3014-1)
for i in range (ulang_3014):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_3014)
for i in range(1,ulang_3014+1):
    print(i, end=" ")