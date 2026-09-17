#Buat file dengan assignment_NIM.py
#Nma variabel ditambah 4 digit nim terakhir contoh : angka_1234
# Program ini menggunakan fungsi input ()
#Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
#Program operator assignment dalam Python

angka1_3014 = int(input("Input angka-1: "))
angka2_3014 = int(input("Input angka-2: "))

print("\nNilai awal angka =", angka1_3014)
print("Nilai angka2 = ", angka2_3014)

#Assigment biasa
hasil_3014 = angka1_3014
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3014)

#Assignment penambahan
hasil_3014 = angka1_3014
hasil_3014 += angka2_3014
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3014)

#Assignment pengurangan
hasil_3014 = angka1_3014
hasil_3014 -= angka2_3014
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3014)

#Assignment perkalian
hasil_3014 = angka1_3014
hasil_3014 *= angka2_3014
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3014)

#Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3014 !=0:
    hasil_3014 = angka1_3014
    hasil_3014 /= angka2_3014
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil_3014)
    #Operator tambahan
    hasil_3014 = angka1_3014
    hasil_3014 //= angka2_3014
    print("nAssignment pembagian bulat (//=)")
    print("Hasil = ", hasil_3014)
    hasil_3014 = angka1_3014
    hasil_3014 %= angka2_3014
    print("nAssignment sisa bagi ( %= ")
    print("hasil =", hasil_3014)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

#operator tambahan: assignment perpangkatan 
hasil_3014 = angka1_3014
hasil_3014 **= angka2_3014
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3014)