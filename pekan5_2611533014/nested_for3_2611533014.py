#Buat file dengan nama nested_for3_2611533014.py
#Buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit NIM terakhir contoh:ulang_1234
#Program ini menggunakan fungsi input ()

batas_3014 = int(input("Masukkan nilai batas: "))
for i in range(batas_3014+1):
    for j in range(batas_3014+1):
        print(i+j, end=" ")
    print() #Pindah ke baris berikutnya