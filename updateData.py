def updateMap(vertices) : # -- Belum terhubung ke map utama di main.py
    print("")
    
    graph = [[0 for column in range(vertices)] for row in range(vertices)]

    graphInput1 = 0
    while graphInput1 != -1 :
        graphInput1 = int(input("Masukkan titik 1: "))
        if (graphInput1 != -1) :
            graphInput2 = int(input("Masukkan titik 2: "))
            distanceInput = int(input("Masukkan jarak: "))
            print("")
            graph[graphInput1][graphInput2] = distanceInput
            graph[graphInput2][graphInput1] = distanceInput

    return graph

def updateSpeed(vertices) :
    roadAVGSpeed = ""
    for i in range(vertices) :
        for j in range(vertices) :
            if (map[i][j] != 0 and j > i) :
                roadAVGSpeed += input("Kecepatan rata-rata di titik " + str(i) + " ke " + str(j) + " (dalam km/jam): ") + "\n"
    
    confirmInput = input("Perbarui data driver? (YA / TIDAK) : ")

    if confirmInput == "YA" :
        with open('keramaian.txt', 'w') as a :
            a.write(roadAVGSpeed)

def updateDriver(vertices) :
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

    confirmInput = input("Perbarui data? (YA / TIDAK) : ")

    if confirmInput == "YA" :
        with open('jumlah ojek.txt', 'w') as a :
            a.write(jumlah)

        with open('namaOjek.txt', 'w') as a :
            a.write(driverName)

        with open('ratingOjek.txt', 'w') as a :
            a.write(driverRating)

