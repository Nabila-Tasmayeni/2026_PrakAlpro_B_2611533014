#Buat file dengan nama if_elif_else1_2611533014.py
#Buat program untuk kondisional if
#Nama variabel ditambah 4 digit NIM terakhir contoh: ipk_1234
#Program ini menggunakan fungsi input ()

umur_3014 = int(input("Input Umur Anda = "))
sim_3014 = input("Apakah Anda Sudah Punya SIM (y/t): ")[0]

if umur_3014 >= 17 and sim_3014 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_3014 >= 17 and sim_3014 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3014 < 17 and sim_3014 == "y":
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai")