from dijkstra import graphMaker, dijkstra
from tempatOjek import tempatOjek

vertices = 9
map = graphMaker(vertices) 
        #0,1, 2, 3, 4, 5, 6, 7, 8
map = [[0, 4, 0, 0, 0, 0, 0, 8, 0], #0
           [4, 0, 8, 0, 0, 0, 0, 11, 0], #1
           [0, 8, 0, 7, 0, 4, 0, 0, 2], #2
           [0, 0, 7, 0, 9, 14, 0, 0, 0], #3
           [0, 0, 0, 9, 0, 10, 0, 0, 0], #4
           [0, 0, 4, 14, 10, 0, 2, 0, 0], #5
           [0, 0, 0, 0, 0, 2, 0, 1, 6], #6
           [8, 11, 0, 0, 0, 0, 1, 0, 7], #7 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] # 8 
           ]

lokasiOjek = tempatOjek(vertices)
print(lokasiOjek)
lokasiPenumpang = int(input("Masukkan node ke berapa penumpang berada : "))
dijkstraAwal = dijkstra(lokasiPenumpang,vertices,map)
dijkstraAkhir = [0 for i in range(vertices)]
print(dijkstraAwal)
for i in range (vertices):
    if lokasiOjek[i] == 0:
        dijkstraAkhir[i] = 0
    else :
        dijkstraAkhir[i] = dijkstraAwal[i]
 
print(dijkstraAkhir)

