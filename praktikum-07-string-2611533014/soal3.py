# Name: Nabila Tasmayeni
# NIM: 2611533014
# Question 3

#soal a
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

#soal b
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)


text = "Nabila Tasmayeni"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)