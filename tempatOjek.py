def tempatOjek(vertices) :
    arrayOjek = [0 for i in range (vertices)]
    for i in range (vertices) :
        jumlah = int(input(f"Masukkan jumlah ojek di node ke-{i}: "))
        arrayOjek[i] = jumlah
    return arrayOjek
    