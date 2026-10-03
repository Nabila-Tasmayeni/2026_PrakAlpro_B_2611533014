print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")

n_3014 = int(input("Masukkan ukuran skala jam pasir (N): "))

if n_3014 <= 0:
    print("N harus bilangan positif!")
else:

    # Border atas
    print("#", end="")
    for i_3014 in range(4 * n_3014 + 5):
        print("=", end="")
    print("#")

    # Jam pasir bagian atas
    for baris_3014 in range(n_3014, 0, -1):

        print("|", end="")

        # Spasi kiri
        print(" ", end="")
        for spasi_3014 in range(2 * (n_3014 - baris_3014)):
            print(" ", end="")

        # Angka menurun
        for angka_3014 in range(baris_3014, 0, -1):
            print(angka_3014, end=" ")

        # Poros kristal
        print("<*>", end="")

        # Angka menaik
        for angka_3014 in range(1, baris_3014 + 1):
            print(" ", end="")
            print(angka_3014, end="")

        # Spasi kanan
        for spasi_3014 in range(2 * (n_3014 - baris_3014)):
            print(" ", end="")

        print(" |")

    # Titik pusat
    print("|", end="")

    for spasi_3014 in range(2 * n_3014 + 1):
        print(" ", end="")

    print("<*>", end="")

    for spasi_3014 in range(2 * n_3014 + 1):
        print(" ", end="")

    print("|")

    # Jam pasir bagian bawah
    for baris_3014 in range(1, n_3014 + 1):

        print("|", end="")

        # Spasi kiri
        print(" ", end="")
        for spasi_3014 in range(2 * (n_3014 - baris_3014)):
            print(" ", end="")

        # Angka menurun
        for angka_3014 in range(baris_3014, 0, -1):
            print(angka_3014, end=" ")

        # Poros kristal
        print("<*>", end="")

        # Angka menaik
        for angka_3014 in range(1, baris_3014 + 1):
            print(" ", end="")
            print(angka_3014, end="")

        # Spasi kanan
        for spasi_3014 in range(2 * (n_3014 - baris_3014)):
            print(" ", end="")

        print(" |")

    # Border bawah
    print("#", end="")
    for i_3014 in range(4 * n_3014 + 5):
        print("=", end="")
    print("#")