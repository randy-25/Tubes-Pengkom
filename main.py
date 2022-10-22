from numpy import true_divide
from dijkstra import graphMaker, dijkstra
from tempatOjek import tempatOjek
import os

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

def userMain():
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

    def zeroMaker(dijkstraInitial, dijkstraFinal) :
        for i in range (vertices):
            if lokasiOjek[i] == 0:
                dijkstraFinal[i] = 0
            else :
                dijkstraFinal[i] = dijkstraInitial[i]
        return dijkstraFinal

    def getBestIndex() :
        temp = 0
        for i in range(ojekCount()) :
            if driverScore[i] > driverScore[temp] :
                temp = i
        return temp

    def ojekku(int) :
        print("Nama Driver  : " + str(driverName[int]), end='')
        print("Rating       : " + str(driverRating[int]) + "/5")
        print("Waktu tempuh : " + str(driverTime[int]) + "s")
        print("Jarak        : " + str(driverDistance[int]) + "m")
        print("Overall score: " + str(driverScore[int]) + "/6")

    # Proses mendapat input keterangan nama, rating, jarak, dan waktu tempuh
    def driverDetail() :
        driverIndex = 0
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
                    driverScore[driverIndex] = driverRating[driverIndex] + 10 / driverTime[driverIndex]
                    driverIndex += 1
    lokasiOjek = tempatOjek(vertices)

    # Deklarasi array untuk driver ojek
    driverName = ['' for i in range(ojekCount())]
    driverTime = ['' for i in range(ojekCount())]
    driverDistance = ['' for i in range(ojekCount())]
    driverRating = ['' for i in range(ojekCount())]
    driverScore = ['' for i in range(ojekCount())]

    print("Terdapat " + str(ojekCount()) + " ojek di sekitar.\n")
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

    dijkstraAkhir = zeroMaker(dijkstraAwal, dijkstraAkhir)

    print("Waktu tempuh driver ke titik penumpang (dalam s):")
    print(dijkstraAkhir)
    print("")
    print(lokasiOjek)
    mapDistanceInitial = dijkstra(lokasiPenumpang, vertices, map)
    mapDistanceFinal = [0 for i in range(vertices)]
    mapDistanceFinal = zeroMaker(mapDistanceInitial, mapDistanceFinal)

    driverDetail()

    if driverTime[getBestIndex()] < 60 :
        strTime = "< 1 menit"
    else :
        strTime = "+-" + str(driverTime[getBestIndex()] // 60 + 1) + " menit" 

    print("")

    print("Driver terbaik untukmu: " + str(driverName[getBestIndex()]), end='')
    print("Berjarak " + str(driverDistance[getBestIndex()]) + "m dari kamu dan memiliki rating " + str(driverRating[getBestIndex()]) + "/5")
    print("Estimasi waktu sampai: " + strTime)

    print("")
    while True :
        inputIndex = int(input("Cari Ojek    : "))
        ojekku(inputIndex)
        print("")

userLoginFile = open("loginUser.txt","a+")
userPasswordFile = open("passwordUser.txt","a+")

adminLogin = "admin"
adminPassword = "admin"

while True:
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
        print("Program Mencari Ojek Online Sederhana")
        print("=====================================\n\n")
        adminUser = input("Username Admin : ")
        adminPass = input("Admin Password : ")
        if adminUser == adminLogin and adminPass == adminPassword :
            pass
        else :
            print("invalid Credentials")
            input("Press Enter")
    elif loginChoice == "2":
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
            for i in range (len(loginUser)) :
                if user == loginUser[i] and password == passwordUser[i] :
                    os.system('cls')
                    userMain()
                else :
                    counting += 1
            if counting >= len(loginUser) :
                print("Invalid Credentials")
                input("Press Enter")
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
    elif loginChoice == "3" :
        print("\n\n=====================================")
        print("Closing Program")
        break

userLoginFile.close()
userPasswordFile.close()
            
