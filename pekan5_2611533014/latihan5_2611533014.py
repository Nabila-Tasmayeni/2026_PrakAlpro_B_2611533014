tinggi_3014 = int(input("Masukkan tinggi segitiga: "))

for i_3014 in range(1, tinggi_3014 +1):
    for j_3014 in range(tinggi_3014 - i_3014):
        print(" ", end="")
        
    for j_3014 in range(i_3014):
        print("* ", end="")
        
    print()