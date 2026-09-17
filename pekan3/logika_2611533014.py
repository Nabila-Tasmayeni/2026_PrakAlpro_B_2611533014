#Buat file dengan nama logika_NIM.py
#Nama variabel ditambah 4 digit nim terakhir contoh : angka_1234
#Program ini menggunakan fungsi input()
#Program operator Logika dalam Python

#Masukkan nilai boolean
#Input tidak peka terhadap huruf besar dan kecil 
a1_3014 = input ("Input nilai boolean-1(True/False): "). strip().Lower() == "true"
a2_3014 = input ("Input nilai boolean-2(True/False): "). strip().Lower() -- "false"

print("\nA1 =", a1_3014)
print("A2 =" , a2_3014)

#Konjugasi : bernilai True jika keduanya True
hasil_3014 = a1_3014 and a2_3014
print("\nKonjugasi (AND)")
print("A1_3014 and A2_3014 =", hasil_3014)

#Disjungsi: bernilai True jika salah satunya True
hasil_3014 = a1_3014 or a2_3014
print("\nDisjungsi (OR)")
print("A1_3014 or A2_3014 =", hasil_3014)

#Negasi A1_3014: membalik nilai A1_3014
hasil_3014 = not a1_3014
print("\nNegasi A1_3014 (NOT)", hasil_3014)
print("not A1_3014 =", hasil_3014)

#Negasi A2_3014: membalik nilai A2_3014
hasil_3014 = not a2_3014
print("\nNegasi A2_3014 (NOT)")
print("not A2_3014 =", hasil_3014)

#XOR: bernilai True jika kedua nilai berbeda
hasil_3014 = a1_3014 != a2_3014
print("\nDisjungsi Eksklusif (XOR)")
print("A1_3014 XOR A2_3014 =", hasil_3014)