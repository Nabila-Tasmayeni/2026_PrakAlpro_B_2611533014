kelas = input().split()
pengumpul = input().split()

kelas_set = set(kelas)
pengumpul_set = set(pengumpul)

sudah = kelas_set & pengumpul_set
belum = kelas_set - pengumpul_set

print("Submitted:", len(sudah), "students")
print("Not submitted:", len(belum), "students")

for nomor in kelas:
    if nomor in belum:
        print(nomor)
