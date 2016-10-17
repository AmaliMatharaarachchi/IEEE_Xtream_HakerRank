#n, 1 <= n <= 1000, specifying how many days Joe will be making tacos
#s- shells
#m- meat
#r-rice
#b-beans


days=input()

for l in range(days):
    smdb=[long(i) for i in raw_input().split(" ")]
    s=smdb[0]
    mdb=smdb[1:]
    tot=0
    while(len(mdb)>2):
        max1 = max(mdb)
        # =8
        min1 = min(mdb)
        #=3
        min2 = min(mdb) - (min1 / 2)
        #2
        mdb.remove(max1)
        # 8, 3

        mdb.remove(min1)
        #8
        mdb.append(max1 - min2)
        if(min1/2>0):
            mdb.append(min1/2)
        #8, 5,1
        tot += min2
    tot += min(mdb[0], mdb[1])
    if(s<tot):
        print s

    else:
        print tot
