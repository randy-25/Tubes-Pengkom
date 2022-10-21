vertices = 18
driverIndex = 0
driverName = ""
driverRating = ""
jumlah = ""

for i in range(vertices) :
    ojekCount = int(input(f"Masukkan jumlah ojek di node ke-{i}: "))
    jumlah += str(ojekCount) + "\n"
    if (ojekCount != 0) :
        for j in range(ojekCount) :
            driverName += input("Nama driver " + str(j + 1) + " di node " + str(i) + ": ") + "\n"
            driverRating += input("Rating: ") + "\n"
            driverIndex += 1
    print("")

# print(jumlah)
# print(driverName)
# print(driverRating)
confirmInput = input("Perbarui data? (YA / TIDAK) : ")
if confirmInput == "YA" :
    with open('jumlah ojek.txt', 'w') as a :
        a.write(jumlah)

    with open('namaOjek.txt', 'w') as a :
        a.write(driverName)

    with open('ratingOjek.txt', 'w') as a :
        a.write(driverRating)
else :
    print("Closing program...")