#Buat file dengan nama nested_for1_2611533014.py
#Buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit NIM terakhir contoh:ulang_1234
#Program ini menggunakan fungsi input ()

batas_3014 = int(input("Masukkan nilai batas: "))
for line_3014 in range(1,batas_3014 +1):
    for j_3014 in range(1, (-1* line_3014  + batas_3014 + 1)):
        print("*", end=" ")
    print(line_3014)