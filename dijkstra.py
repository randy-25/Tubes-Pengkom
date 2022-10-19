'''
SOME NOTES
sptSet = penanda jika vertex sudah dihampiri
vertex = node (silahkan baca ini https://en.wikipedia.org/wiki/Vertex_(graph_theory))
vertices = vertex bentuk plural
parameter dijkstra = tempat asal(misal penumpang), jumlah vertex, map (3 parameter karena belum dibolehkan menggunakan class)
return value dari dijkstra = list jarak terdekat dari masing2 vertex ke tempat asal
'''
'''
code sources = https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
'''
def graphMaker(vertices) :
    graph = [[0 for column in range(vertices)] for row in range(vertices)]
    return graph

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


