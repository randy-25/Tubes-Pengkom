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

def mapFinal(vertices) :
    mapFinal = graphMaker(vertices)

    print("\nKecepatan rata-rata kendaraan pada jalan berdasarkan keramaian: ")
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

lokasiOjek = tempatOjek(vertices)
print(lokasiOjek)
lokasiPenumpang = int(input("Masukkan node ke berapa penumpang berada : "))
dijkstraAwal = dijkstra(lokasiPenumpang,vertices,mapFinal(vertices))
dijkstraAkhir = [0 for i in range(vertices)]
print(dijkstraAwal)
for i in range (vertices):
    if lokasiOjek[i] == 0:
        dijkstraAkhir[i] = 0
    else :
        dijkstraAkhir[i] = dijkstraAwal[i]
 
print(dijkstraAkhir)

def ojekCount() :
    count = 0
    for i in lokasiOjek :
        if (i != 0) :
            count += i
    return count

driverName = ['' for i in range(ojekCount())]
driverDistance = ['' for i in range(ojekCount())]
driverRating = ['' for i in range(ojekCount())]
driverScore = ['' for i in range(ojekCount())]

driverIndex = 0

for i in range(vertices) :
    if (lokasiOjek[i] != 0) :
        for j in range(lokasiOjek[i]) :
            driverName[driverIndex] = input("Nama driver " + str(j + 1) + " di node " + str(i) + ": ")
            driverRating[driverIndex] = float(input("Rating: "))
            driverDistance[driverIndex] = dijkstraAkhir[i]
            driverIndex += 1

def ojekku(int) :
    print(driverName[int])
    print(driverRating[int])
    print(driverDistance[int])