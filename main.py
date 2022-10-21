from dijkstra import graphMaker, dijkstra
from tempatOjek import tempatOjek

vertices = 18
map = graphMaker(vertices) 

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

with open('keramaian.txt') as f:
    roadTextInput = f.readlines()

with open('namaOjek.txt') as f:
    nameTextInput = f.readlines()

with open('ratingOjek.txt') as f:
    ratingTextInput = f.readlines()

def mapFinal(vertices) :
    mapFinal = graphMaker(vertices)
    #print("\nKecepatan rata-rata kendaraan pada jalan berdasarkan keramaian: ")
    count = 0
    for i in range(vertices) :
        for j in range(vertices) :
            if (map[i][j] != 0 and mapFinal[i][j] == 0) :
                # roadAVGSpeed = int(input("Kecepatan rata-rata di titik " + str(i) + " ke " + str(j) + " (dalam km/jam): ")) * 1000 / 3600
                roadAVGSpeed = int(roadTextInput[count]) * 1000 / 3600
                mapFinal[i][j] = int(map[i][j] / roadAVGSpeed)
                mapFinal[j][i] = mapFinal[i][j]
                count += 1
    
    return mapFinal

def ojekCount() :
    count = 0
    for i in lokasiOjek :
        if (i != 0) :
            count += i
    return count

lokasiOjek = tempatOjek(vertices)

print("Terdapat " + str(ojekCount()) + " ojek di sekitar.\n")
lokasiPenumpang = int(input("Masukkan node ke berapa penumpang berada : "))

print("Array jumlah ojek di setiap node:")
print(lokasiOjek)
print("")

dijkstraAwal = dijkstra(lokasiPenumpang,vertices,mapFinal(vertices))
dijkstraAkhir = [0 for i in range(vertices)]

print("Waktu tempuh dari setiap node ke titik penumpang (dalam s):")
print(dijkstraAwal)
print("")

def zeroMaker(dijkstraInitial, dijkstraFinal) :
    for i in range (vertices):
        if lokasiOjek[i] == 0:
            dijkstraFinal[i] = 0
        else :
            dijkstraFinal[i] = dijkstraInitial[i]
    return dijkstraFinal

dijkstraAkhir = zeroMaker(dijkstraAwal, dijkstraAkhir)

print("Waktu tempuh driver ke titik penumpang (dalam s):")
print(dijkstraAkhir)
print("")

# Deklarasi array untuk driver ojek
driverName = ['' for i in range(ojekCount())]
driverTime = ['' for i in range(ojekCount())]
driverDistance = ['' for i in range(ojekCount())]
driverRating = ['' for i in range(ojekCount())]
driverScore = ['' for i in range(ojekCount())]

driverIndex = 0

mapDistanceInitial = dijkstra(lokasiPenumpang, vertices, map)
mapDistanceFinal = [0 for i in range(vertices)]
mapDistanceFinal = zeroMaker(mapDistanceInitial, mapDistanceFinal)

# Proses mendapat input keterangan nama, rating, jarak, dan waktu tempuh
for i in range(vertices) :
    if (lokasiOjek[i] != 0) :
        for j in range(lokasiOjek[i]) :
            # driverName[driverIndex] = input("Nama driver " + str(j + 1) + " di node " + str(i) + ": ")
            # driverRating[driverIndex] = float(input("Rating: "))
            driverName[driverIndex] = nameTextInput[driverIndex]
            driverRating[driverIndex] = float(ratingTextInput[driverIndex])
            driverDistance[driverIndex] = mapDistanceFinal[i]
            if dijkstraAkhir[i] == 0 :
                driverTime[driverIndex] = dijkstraAkhir[i] + 10
            else :
                driverTime[driverIndex] = dijkstraAkhir[i]
            driverScore[driverIndex] = driverRating[driverIndex] + 1 / driverTime[driverIndex]
            driverIndex += 1

def getBestIndex() :
    temp = 0
    for i in range(ojekCount()) :
        if driverScore[i] > driverScore[temp] :
            temp = i
    return temp

if driverTime[getBestIndex()] < 60 :
    strTime = "< 1 menit"
else :
    strTime = "+-" + str(driverTime[getBestIndex()] // 60 + 1) + " menit"

def ojekku(int) :
    print("Nama Driver  : " + str(driverName[int]), end='')
    print("Rating       : " + str(driverRating[int]) + "/5")
    print("Waktu tempuh : " + str(driverTime[int]) + "s")
    print("Jarak        : " + str(driverDistance[int]) + "m")
    print("Overall score: " + str(driverScore[int]) + "/6") 

print("")

print("Driver terbaik untukmu: " + str(driverName[getBestIndex()]), end='')
print("Berjarak " + str(driverDistance[getBestIndex()]) + "m dari kamu dan memiliki rating " + str(driverRating[getBestIndex()]) + "/5")
print("Estimasi waktu sampai: " + strTime)

print("")

while True :
    inputIndex = int(input("Cari Ojek    : "))
    ojekku(inputIndex)
    print("")