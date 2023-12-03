import itertools 
file = open('Day2/input.txt', 'r')
data = file.readlines()
cubes = {
'red' : 0,
'blue' : 0,
'green' : 0
}
# tot = r_c + b_c + g_c
correct = []
# temp = data[0].split(';')[1]#.split('Game 1:')[1]
# print(temp)
# temp = temp.split(' ')
# temp.pop(0)
# print(temp)
for i in range(len(data)):
    data[i] = data[i].rstrip('\n')


for i, j in enumerate(data):
    cubes = {
'red' : 0,
'blue' : 0,
'green' : 0
}
    tl = []
    temp = j.split(';')
    for k in range(len(temp)):
        s = 'Game ' + str(i+1) + ':'
        if k == 0:
            t = temp[k].split(s)
            t.pop(0)
            t = t[0].split(' ')
            t.pop(0)
            t = t[::-1]
            for m in range(len(t)):
                t[m] = t[m].rstrip(',')
            t = dict(itertools.zip_longest(*[iter(t)]*2, fillvalue=""))
            tl.append(t)
        else:
            t = temp[k].split(' ')
            t.pop(0)
            t = t[::-1]
            for m in range(len(t)):
                t[m] = t[m].rstrip(',')
            t = dict(itertools.zip_longest(*[iter(t)]*2, fillvalue=""))
            tl.append(t)
    # mr, mb, mg = 0, 0, 0
    for d in tl:
        for e in d.keys():
            if int(d[e]) > cubes[e]:
                cubes[e] = int(d[e])
    s=1
    for p in cubes.values():
        s*=p
    correct.append(s)

print(sum(correct))
    