lst = [[i*j for i in range(1,11)] for j in range(1,11)]
for i in lst:
    for j in i:
        if len(str(j))==1:
            print(j, end='  ')
        elif len(str(j)) == 2:
            print(j, end=' ')
        else: print(j, end='')
    print()