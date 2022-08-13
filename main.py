for k in [6,10]:
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for i in list(range(k-4,k)):
            print(f"{i:2d} *{j:2d} = {i*j:2d}", end="  ")
        print("")
    print("")