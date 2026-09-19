#Buat file dengan nama aritmatika_NIM.py
#Buat program untuk operator aritmatika dalam Python
#Nma variabel ditambah 4 digit nim terakhir contoh :angka_1234
#Program ini menggunakan fungsi input()
#Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3014 = int(input("Input angka-1="))
angka2_3014 = int(input("Input angka-2="))

# Penjumlahan
hasil_3014 =angka1_3014 + angka2_3014
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3014)

#Pengurangan
hasil_3014 = angka1_3014 - angka2_3014
print("\nOperator Pengurangan")
print("Hasil =", hasil_3014)

#Perkalian
hasil_3014 = angka1_3014 * angka2_3014
print("\nOperator Perkalian")
print("Hasil =", hasil_3014)

#Pembagian, pembagian bulat, dan sisa bagi
if angka2_3014 != 0:
    hasil_3014 = angka1_3014 / angka2_3014
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3014)

    hasil_3014 = angka1_3014 // angka2_3014
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3014)

    hasil_3014 = angka1_3014 % angka2_3014
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3014)
else:
    print("Angka kedua tidak bole bernilai 0,")

# Pangkat
hasil_3014 = angka1_3014 ** angka2_3014
print("\nOperator Pangkat")
print("Hasil =", hasil_3014)