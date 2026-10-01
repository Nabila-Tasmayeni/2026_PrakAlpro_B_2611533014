#Buat file dengan nama jumlah_genap_2611533014.py
#Buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit NIM terakhir contoh:ulang_1234
#Program ini menggunakan fungsi input ()

ulang_3014 = int(input("Masukkan jumlah perulangan: "))

jumlah_3014 = 0
for i in range(1, ulang_3014+1):
    if i % 2 == 0:
        print(i,end=" ")
        jumlah_3014 = jumlah_3014 + i

        if i < ulang_3014:
            print("+",end="")
        else:
            print("=", jumlah_3014,end="")
print()
print("jumlah_3014 =", jumlah_3014)   