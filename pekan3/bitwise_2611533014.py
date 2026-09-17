#Buat file dengan nama Bitwise_NIM.py
#Nma variabel ditambah 4 digit nim terakhir contoh: angka1_1234
#Program ini menggunakan fungsi input()

print("\n==================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_3014 = int(input("Masukkan angka bitwise-1:"))
angka2_3014 = int(input("Masukkan angka bitwise-2:"))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_3014 =", angka1_3014, "| biner =", bin(angka1_3014))
print("angka2_3014 =", angka2_3014, "| biner =", bin(angka2_3014))

#Bitwise AND
hasil_3014 = angka1_3014 & angka2_3014
print("\nBitwise AND (&)")
print("angka1_3014 & angka2_3014 =", hasil_3014)
print("Biner hasil =", bin(hasil_3014))
print("Biner hasil (8 bit) =", format(hasil_3014, '08b'))

#Bitwise OR
hasil_3014 = angka1_3014 | angka2_3014
print("\nBitwise OR (|)")
print("angka1_3014 | angka2_3014 =", hasil_3014)
print("Biner hasil =", bin(hasil_3014))
print("Biner hasil (8 bit) =", format(hasil_3014, '08b'))

#Bitwise XOR
hasil_3014 = angka1_3014 ^ angka2_3014
print("\nBitwise XOR (^)")
print("angka1_3014 ^ angka2_3014 =", hasil_3014)
print("Biner hasil =", bin(hasil_3014))
print("Biner hasil (8 bit) =", format(hasil_3014, '08b'))

#Bitwise NOT
hasil_3014 = ~angka1_3014
print("\nBitwise NOT (~)")
print("~angka1_3014 =", hasil_3014)
print("Biner hasil =", bin(hasil_3014))
print("Biner hasil (8 bit) =", format(hasil_3014, '08b'))

#Bitwise geser ke kiri
jumlah_geser_3014 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3014 = angka1_3014 << jumlah_geser_3014
print("\nBitwise geser ke kiri (<<)")
print("angka1_3014 <<", jumlah_geser_3014, "=", hasil_3014)
print("Biner hasil =", bin(hasil_3014))
print("Biner hasil (8 bit) =", format(hasil_3014, '08b'))

#Bitwise geser kanan
hasil_3014 = angka1_3014 >> jumlah_geser_3014
print("\nBitwise geser kanan (>>)")
print(angka1_3014, ">>", jumlah_geser_3014, "=", hasil_3014)
print("Biner hasil =", bin(hasil_3014))
print("Biner hasil (8 bit) =", format(hasil_3014, "08b"))