import os
import time

with open('map.txt') as mapFile :
    mapTextInput = mapFile.readlines()

with open('jumlah ojek.txt') as jumlahOjekFile:
    ojekTextInput = jumlahOjekFile.readlines()

with open('keramaian.txt') as keramaianFile:
    roadTextInput = keramaianFile.readlines()

with open('namaOjek.txt') as namaOjekFile:
    nameTextInput = namaOjekFile.readlines()

with open('ratingOjek.txt') as ratingOjekFile:
    ratingTextInput = ratingOjekFile.readlines()

def loadingScreen(duration) :
    print("░█████╗░░░░░░░░░░░░██╗███████╗██╗░░██╗")
    print("██╔══██╗░░░░░░░░░░░██║██╔════╝██║░██╔╝")
    print("██║░░██║█████╗░░░░░██║█████╗░░█████═╝░")
    print("██║░░██║╚════╝██╗░░██║██╔══╝░░██╔═██╗░")
    print("╚█████╔╝░░░░░░╚█████╔╝███████╗██║░╚██╗")
    print("░╚════╝░░░░░░░░╚════╝░╚══════╝╚═╝░░╚═╝")
    print("\n               LOADING")
    animation = [
        "         [                 ]",
        "         [=                ]",
        "         [===              ]",
        "         [====             ]",
        "         [=====            ]",
        "         [======           ]",
        "         [=======          ]",
        "         [========         ]",
        "         [=========        ]",
        "         [==========       ]",
        "         [===========      ]",
        "         [============     ]",
        "         [=============    ]",
        "         [==============   ]",
        "         [===============  ]",
        "         [================ ]",
        "         [=================]"
        ]
    count = 0
    for i in animation :
        print(animation[count % arrayLength(animation)], end='\r')
        time.sleep(duration / 100)
        count +=1

def graphMaker(vertices) :
    graph = [[0 for column in range(vertices)] for row in range(vertices)]
    return graph

def verticesCount(count) :
    x = 0
    while (x**2 != count) :
        x += 1
    return x

def arrayLength(arr) :
    count = 0
    for i in arr :
        count += 1
    return count
    
vertices = verticesCount(arrayLength(mapTextInput))
map = graphMaker(vertices)

for i in range(vertices**2) :
    map[i // vertices][i % vertices] = int(mapTextInput[i])

# map = [[0, 250, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [250, 0, 50, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 50, 0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 150, 0, 0, 0, 0, 0],
#         [0, 150, 0, 0, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 150, 50, 0, 0, 0, 0, 0, 100, 200, 150, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 50, 0, 0, 100, 150, 150, 100, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 100, 0, 150, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 150, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 150, 50, 0, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 100, 100, 0, 0, 200, 0, 150, 0, 0, 0, 0, 0, 250, 0],
#         [0, 0, 0, 0, 200, 0, 0, 0, 0, 150, 0, 100, 0, 200, 150, 0, 150, 0],
#         [0, 0, 0, 0, 150, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0, 0, 150, 0, 200, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 150, 0, 0, 150, 0, 100, 150, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 250, 150, 0, 0, 200, 150, 0, 0,50],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0]]

def minDistance(dist,sptSet,vertices) :
    min = 1e7
    for i in range(vertices) :
        if dist[i] < min and sptSet[i] == False :
            min = dist[i] 
            min_index = i
    return min_index


def dijkstra(src, vertices, map) :
    dist = [1e7]*vertices
    dist[src] = 0
    sptSet = [False] * vertices
    '''
    #DEBUG
    print(sptSet)
    print(dist)
    '''
    for j in range(vertices) :
        '''
        #DEBUG
        print()
        print(dist)
        print(sptSet)
        '''
        # u pertama pasti sama dengan tempat asal
        u = minDistance(dist,sptSet,vertices)
        # DEBUG
        #print("u = ",u)
        sptSet[u] = True
        for k in range(vertices) :
            '''
            DEBUG
            print(f"map[{u}][{k}]", map[u][k])
            print(f"sptset[{k}]", sptSet[k])
            print(f"dist[{k}]",dist[k])
            print(f"dist[{u}] + map[{u}][{k}]", dist[u] + map[u][k])
            '''
            
            if map[u][k] > 0 and sptSet[k] == False and dist[k] > dist[u] + map[u][k] :
                dist[k] = dist[u] + map[u][k]
                '''
                # DEBUG
                print("jalan")
                '''
    return dist

def tempatOjek(vertices) :
    arrayOjek = [0 for i in range (vertices)]
    for i in range (vertices) :
        #jumlah = int(input(f"Masukkan jumlah ojek di node ke-{i}: "))
        jumlah = int(ojekTextInput[i])
        arrayOjek[i] = jumlah
    return arrayOjek

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

def ojekCount(lokasiOjek) :
    count = 0
    for i in lokasiOjek :
        if (i != 0) :
            count += i
    return count

def zeroMaker(dijkstraInitial, dijkstraFinal, lokasiOjek) :
    for i in range (vertices):
        if lokasiOjek[i] == 0:
            dijkstraFinal[i] = 0
        else :
            dijkstraFinal[i] = dijkstraInitial[i]
    return dijkstraFinal

def getBestIndex(driverScore) :
    temp = 0
    for i in range(ojekCount(lokasiOjek)) :
        if driverScore[i] > driverScore[temp] :
            temp = i
    return temp

# Proses mendapat input keterangan nama, rating, jarak, dan waktu tempuh
def driverDetail(driverName, driverTime, driverDistance, driverRating, driverScore, lokasiOjek, dijkstraAkhir, mapDistanceFinal) :
    driverIndex = 0
    for i in range(vertices) :
        if (lokasiOjek[i] != 0) :
            for j in range(lokasiOjek[i]) :
                # driverName[driverIndex] = input("Nama driver " + str(j + 1) + " di node " + str(i) + ": ")
                # driverRating[driverIndex] = float(input("Rating: "))
                driverName[driverIndex] = nameTextInput[driverIndex]
                driverRating[driverIndex] = float(ratingTextInput[driverIndex])
                driverDistance[driverIndex] = mapDistanceFinal[i]
                # if dijkstraAkhir[i] == 0 :
                #     driverTime[driverIndex] = dijkstraAkhir[i] + 10
                # else :
                #     driverTime[driverIndex] = dijkstraAkhir[i]
                driverTime[driverIndex] = dijkstraAkhir[i]
                driverScore[driverIndex] = driverRating[driverIndex] + 10 / ((driverTime[driverIndex] ** (1/3)) + 10)
                driverIndex += 1

def userMain(driverName, driverTime, driverDistance, driverRating, driverScore):
    os.system('cls')
    print("Program Mencari Ojek Online Sederhana")
    print("=====================================\n\n")

    print("Terdapat " + str(ojekCount(lokasiOjek)) + " ojek di sekitar.\n")
    lokasiPenumpang = int(input("Pilih titik penjemputan (0-" + str(vertices - 1) + "): "))
    print("")

    os.system('cls')
    loadingScreen(5)
    os.system('cls')

    # print("Array jumlah ojek di setiap node:")
    # print(lokasiOjek)
    # print("")

    dijkstraAwal = dijkstra(lokasiPenumpang,vertices,mapFinal(vertices))
    dijkstraAkhir = [0 for i in range(vertices)]

    # print("Waktu tempuh dari setiap node ke titik penumpang (dalam s):")
    # print(dijkstraAwal)
    # print("")

    dijkstraAkhir = zeroMaker(dijkstraAwal, dijkstraAkhir, lokasiOjek)

    # print("Waktu tempuh driver ke titik penumpang (dalam s):")
    # print(dijkstraAkhir)
    # print("")
    # print(lokasiOjek)
    mapDistanceInitial = dijkstra(lokasiPenumpang, vertices, map)
    mapDistanceFinal = [0 for i in range(vertices)]
    mapDistanceFinal = zeroMaker(mapDistanceInitial, mapDistanceFinal, lokasiOjek)

    driverDetail(driverName, driverTime, driverDistance, driverRating, driverScore, lokasiOjek, dijkstraAkhir,mapDistanceFinal)
    
    if driverTime[getBestIndex(driverScore)] < 60 :
        strTime = "< 1 menit"
    else :
        strTime = "+-" + str(driverTime[getBestIndex(driverScore)] // 60 + 1) + " menit" 

    print("")

    print("Driver terbaik untukmu: " + str(driverName[getBestIndex(driverScore)]), end='')
    print("Berjarak " + str(driverDistance[getBestIndex(driverScore)]) + "m dari kamu dan memiliki rating " + str(driverRating[getBestIndex(driverScore)]) + "/5")
    print("Estimasi waktu sampai: " + strTime)

    print("")
    print("\n\t   Program Selesai")
    print("=====================================")
    input("Closing Program\n\n")

def ojekku(int) :
    print("Nama Driver  : " + str(driverName[int]), end='')
    print("Rating       : " + str(driverRating[int]) + "/5")
    print("Waktu tempuh : " + str(driverTime[int]) + "s")
    print("Jarak        : " + str(driverDistance[int]) + "m")
    print("Overall score: " + str(driverScore[int]))

def updateMap(vertices) :
    os.system('cls')
    print("Updating Map")
    print("============\n\n")
    mapText = ''
    graph = graphMaker(vertices)

    graphInput1 = 0
    while (graphInput1 != -1) :
        print("Ketik -1 pada titik 1 untuk mengakhiri input")
        graphInput1 = int(input("Masukkan titik 1: "))
        if (graphInput1 != -1) :
            graphInput2 = int(input("Masukkan titik 2: "))
            distanceInput = int(input("Masukkan jarak: "))
            print("")
            graph[graphInput1][graphInput2] = distanceInput
            graph[graphInput2][graphInput1] = distanceInput

    for i in range(vertices) :
        for j in range(vertices) :
            mapText += str(graph[i][j]) + "\n"

    confirmInput = input("Perbarui data map? (YA / TIDAK) : ")

    if confirmInput == "YA" :
        with open('map.txt', 'w') as mapFile :
            mapFile.write(mapText)
    
    updateSpeed(vertices)
    updateDriver(vertices)

def updateSpeed(vertices) :
    os.system('cls')
    print("Updating Keramaian")
    print("==================\n\n")
    roadAVGSpeed = ""
    for i in range(vertices) :
        for j in range(vertices) :
            if (map[i][j] != 0 and j > i) :
                roadAVGSpeed += input("Kecepatan rata-rata di titik " + str(i) + " ke " + str(j) + " (dalam km/jam): ") + "\n"
    
    confirmInput = input("Perbarui data keramaian? (YA / TIDAK) : ")

    if confirmInput == "YA" :
        with open('keramaian.txt', 'w') as a :
            a.write(roadAVGSpeed)

def updateDriver(vertices) :
    os.system('cls')
    print("Updating Driver")
    print("===============\n\n")
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

    confirmInput = input("Perbarui data driver? (YA / TIDAK) : ")

    if confirmInput == "YA" :
        with open('jumlah ojek.txt', 'w') as a :
            a.write(jumlah)

        with open('namaOjek.txt', 'w') as a :
            a.write(driverName)

        with open('ratingOjek.txt', 'w') as a :
            a.write(driverRating)

def adminMain(driverName, driverTime, driverDistance, driverRating, driverScore):
    os.system('cls')
    print("Program Mencari Ojek Online Sederhana")
    print("=====================================\n\n")

    print("Terdapat " + str(ojekCount(lokasiOjek)) + " ojek di sekitar.\n")
    lokasiPenumpang = int(input("Masukkan node ke berapa penumpang berada : "))
    print("")

    print("Array jumlah ojek di setiap node:")
    print(lokasiOjek)
    print("")

    dijkstraAwal = dijkstra(lokasiPenumpang,vertices,mapFinal(vertices))
    dijkstraAkhir = [0 for i in range(vertices)]

    print("Waktu tempuh dari setiap node ke titik penumpang (dalam s):")
    print(dijkstraAwal)
    print("")

    dijkstraAkhir = zeroMaker(dijkstraAwal, dijkstraAkhir, lokasiOjek)

    print("Waktu tempuh driver ke titik penumpang (dalam s):")
    print(dijkstraAkhir)
    print("")
    print(lokasiOjek)
    mapDistanceInitial = dijkstra(lokasiPenumpang, vertices, map)
    mapDistanceFinal = [0 for i in range(vertices)]
    mapDistanceFinal = zeroMaker(mapDistanceInitial, mapDistanceFinal, lokasiOjek)

    driverDetail(driverName, driverTime, driverDistance, driverRating, driverScore, lokasiOjek, dijkstraAkhir,mapDistanceFinal)
    print()
    for i in range(ojekCount(lokasiOjek)) :
        ojekku(i)
        print("")
    input("\n\nPress Enter")

lokasiOjek = tempatOjek(vertices)

# Deklarasi array untuk driver ojek
driverName = ['' for i in range(ojekCount(lokasiOjek))]
driverTime = ['' for i in range(ojekCount(lokasiOjek))]
driverDistance = ['' for i in range(ojekCount(lokasiOjek))]
driverRating = ['' for i in range(ojekCount(lokasiOjek))]
driverScore = ['' for i in range(ojekCount(lokasiOjek))]

userLoginFile = open("loginUser.txt","a+")
userPasswordFile = open("passwordUser.txt","a+")

adminLogin = "admin"
adminPassword = "admin"

while True:
    os.system('cls')
    loadingScreen(5)
    os.system('cls')
    print("Program Mencari Ojek Online Sederhana")
    print("=====================================\n\n")
    userLoginFile.seek(0)
    loginUser = userLoginFile.readlines()
    userPasswordFile.seek(0)
    passwordUser = userPasswordFile.readlines()
    
    print("1. Login Admin")
    print("2. Login User")
    print("3. Keluar dari Program")
    loginChoice = input("Masukkan Pilihan Anda : ")
    if loginChoice == "1" :
        os.system('cls')
        loadingScreen(5)
        os.system('cls')
        print("Program Mencari Ojek Online Sederhana")
        print("=====================================\n\n")
        adminUser = input("Username Admin : ")
        adminPass = input("Admin Password : ")
        if adminUser == adminLogin and adminPass == adminPassword :
            while True :
                os.system('cls')
                print("Program Mencari Ojek Online Sederhana")
                print("=====================================\n\n")
                print("1. Update Map")
                print("2. Update Keramaian")
                print("3. Update Driver")
                print("4. Debug Ojek")
                print("5. Log Out")
                adminChoice = input("Pilihan : ")
                if adminChoice == "1" :
                    vertices = int(input("Masukkan jumlah titik pada map: "))
                    updateMap(vertices)
                elif adminChoice == "2" :
                    updateSpeed(vertices)
                elif adminChoice == "3" :
                    updateDriver(vertices)
                elif adminChoice == "4" :
                    adminMain(driverName, driverTime, driverDistance, driverRating, driverScore)
                elif adminChoice == "5" :
                    break
                else :
                    print("Pilihan Anda Salah")
                    input("Press Enter")
        else :
            print("Invalid Credentials")
            input("Press Enter")
    elif loginChoice == "2":
        os.system('cls')
        loadingScreen(5)
        os.system('cls')
        print("Program Mencari Ojek Online Sederhana")
        print("=====================================\n\n")
        print("1. Login\n2. Buat Akun\n3. Back")
        userChoice = input("1/2/3? ")
        if userChoice == "1" :
            os.system('cls')
            print("Program Mencari Ojek Online Sederhana")
            print("=====================================\n\n")
            user = input("Masukkan Username : ")
            user += "\n"
            password = input("Masukkan Password : ")
            password += "\n"
            counting = 0
            for i in range (arrayLength(loginUser)) :
                if user == loginUser[i] and password == passwordUser[i] :
                    userMain(driverName, driverTime, driverDistance, driverRating, driverScore)
                else :
                    counting += 1
            if counting >= arrayLength(loginUser) :
                print("Invalid Credentials")
                input("Press Enter")
            else :
                break
        elif userChoice == "2":
            os.system('cls')
            print("Program Mencari Ojek Online Sederhana")
            print("=====================================\n\n")
            user = input("Masukkan Username : ")
            user += "\n"
            password = input("Masukkan Password : ")
            password += "\n"
            userLoginFile.write(user)
            userPasswordFile.write(password)
        elif userChoice == "3" :
            pass
        else :
            print("Input Anda Salah")
            input("Press Enter")
    elif loginChoice == "3" :
        print("\n\n=====================================")
        input("Closing Program\n\n")
        break

userLoginFile.close()
userPasswordFile.close()