vertices = 18

map = [[0, 250, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [250, 0, 50, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 50, 0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 150, 0, 0, 0, 0, 0],
        [0, 150, 0, 0, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 150, 50, 0, 0, 0, 0, 0, 100, 200, 150, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 50, 0, 0, 100, 150, 150, 100, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 100, 0, 150, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 150, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 150, 50, 0, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 100, 100, 0, 0, 200, 0, 150, 0, 0, 0, 0, 0, 250, 0],
        [0, 0, 0, 0, 200, 0, 0, 0, 0, 150, 0, 100, 0, 200, 150, 0, 150, 0],
        [0, 0, 0, 0, 150, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0, 0, 150, 0, 200, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 150, 0, 0, 150, 0, 100, 150, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 250, 150, 0, 0, 200, 150, 0, 0,50],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0]]

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

mapUpdate = input("Update map? (YA / TIDAK) : ")
if (mapUpdate == "YA") :
    vertices = int(input("Masukkan jumlah titik pada map: "))
    map = updateMap(vertices)

keramaianUpdate = input("Update keramaian? (YA / TIDAK) : ")
if (keramaianUpdate == "YA") :
    updateSpeed(vertices)

driverUpdate = input("Update driver? (YA / TIDAK) : ")
if (driverUpdate == "YA") :
    updateDriver(vertices)