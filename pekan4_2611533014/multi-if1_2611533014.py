#Buat file dengan nama multi_1f1_nim.py
#Buat program untuk kondisional if
#Nma variabel dirambah 4 digit nim terakhir contoh:ipk_1234
#Program ini menggunakan input ()

umur_3014 = int(input("Input Umur Anda = "))
sim_3014 = input("Apakah Anda Sudah Punya SIM (y/t): ")[0]

if umur_3014 >= 17 and sim_3014 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_3014 >= 17 and sim_3014 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_3014 < 17 and sim_3014 != "y":
    print("Anda Belum Cukup Umur bawa motor")

if umur_3014 < 17 and sim_3014 == "y":
    print("Anda Belum Cukup Umur punya SIM")