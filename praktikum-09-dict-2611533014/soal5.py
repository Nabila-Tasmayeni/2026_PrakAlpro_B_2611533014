n = int(input())

kas = {}
total_cash = 0

for i in range(n):
    data = input().split()
    nama = data[0]
    nominal = int(data[1])

    if nama in kas:
        kas[nama] += nominal
    else:
        kas[nama] = nominal

    total_cash += nominal

for nama, total in kas.items():
    print(nama + ":", total)

print("Total cash:", total_cash)

top_name = ""
top_total = -1

for nama, total in kas.items():
    if total > top_total:
        top_name = nama
        top_total = total

print("Top contributor:", top_name, "(" + str(top_total) + ")")