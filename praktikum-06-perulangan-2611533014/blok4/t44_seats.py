blocked_seat = int(input("Enter blocked seat: "))
for row in range(1, 4):
    print("Row", row, end=": ")
    for column in range(1, 6):
        if column == blocked_seat:
            break  
        print(column, end=" ") 
    print()
