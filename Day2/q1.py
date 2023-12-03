import itertools 
file = open('Day2/input.txt', 'r')
data = file.readlines()
cubes = {
'red' : 12,
'blue' : 14,
'green' : 13
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
    flag = True
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
            for z in t.keys():
                if cubes[z] < int(t[z]):
                    flag = False
        else:
            t = temp[k].split(' ')
            t.pop(0)
            t = t[::-1]
            for m in range(len(t)):
                t[m] = t[m].rstrip(',')
            t = dict(itertools.zip_longest(*[iter(t)]*2, fillvalue=""))
            for z in t.keys():
                # print(cubes[z], int(t[z]), i+1)
                if cubes[z] < int(t[z]):
                    flag = False
    if flag:
        correct.append(i+1)


print(sum(correct))
    