from dijkstra import graphMaker, dijkstra
from tempatOjek import tempatOjek
from updateData import updateMap, updateSpeed, updateDriver
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

with open('jumlah ojek.txt') as jumlahOjekFile:
    ojekTextInput = jumlahOjekFile.readlines()

def tempatOjek(vertices) :
    arrayOjek = [0 for i in range (vertices)]
    for i in range (vertices) :
        #jumlah = int(input(f"Masukkan jumlah ojek di node ke-{i}: "))
        jumlah = int(ojekTextInput[i])
        arrayOjek[i] = jumlah
    return arrayOjek

with open('keramaian.txt') as keramaianFile:
    roadTextInput = keramaianFile.readlines()

with open('namaOjek.txt') as namaOjekFile:
    nameTextInput = namaOjekFile.readlines()

with open('ratingOjek.txt') as ratingOjekFile:
    ratingTextInput = ratingOjekFile.readlines()

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
                if dijkstraAkhir[i] == 0 :
                    driverTime[driverIndex] = dijkstraAkhir[i] + 10
                else :
                    driverTime[driverIndex] = dijkstraAkhir[i]
                driverScore[driverIndex] = driverRating[driverIndex] + 10 / driverTime[driverIndex]
                driverIndex += 1

def userMain(driverName, driverTime, driverDistance, driverRating, driverScore):
    os.system('cls')
    print("Program Mencari Ojek Online Sederhana")
    print("=====================================\n\n")

    print("Terdapat " + str(ojekCount(lokasiOjek)) + " ojek di sekitar.\n")
    lokasiPenumpang = int(input("Masukkan node ke berapa Anda berada : "))
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
    print("Closing Program\n\n")

def ojekku(int) :
    print("Nama Driver  : " + str(driverName[int]), end='')
    print("Rating       : " + str(driverRating[int]) + "/5")
    print("Waktu tempuh : " + str(driverTime[int]) + "s")
    print("Jarak        : " + str(driverDistance[int]) + "m")
    print("Overall score: " + str(driverScore[int]) + "/6")

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
                    map = updateMap(vertices)
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
                    userMain(driverName, driverTime, driverDistance, driverRating, driverScore)
                else :
                    counting += 1
            if counting >= len(loginUser) :
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
        print("Closing Program\n\n")
        break

userLoginFile.close()
userPasswordFile.close()
            
