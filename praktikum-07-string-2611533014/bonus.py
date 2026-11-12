# Name: Nabila Tasmayeni
# NIM: 2611533014
#soal bonus

sentence = input("Masukkan kalimat: ")
clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")