import sys

n = input()

m = input()

k = input()
all = {}

for i in range(k):

    toZoom = []

    char = raw_input()

    for j in range(m):
        toZoom.append(list(raw_input()))

    all[char] = toZoom

x = input()

for t in range(x):
    string = list(raw_input())
    list1 = []
    for s in string:
        list1.append(all[s])



    for l in range(m):
        for lm in range(len(string)):
            if len(list1[lm][l])>0:
                for lmn in list1[lm][l]:
                    sys.stdout.write(lmn)
            else:
                sys.stdout.write(" "*n)
        print ""
