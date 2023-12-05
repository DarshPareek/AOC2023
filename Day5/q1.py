file = open('Day5/input.txt' , 'r')
types = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
seeds = file.readline().rstrip('\n').split('seeds: ')
seeds.pop(0)
seeds = seeds[0].split(' ')
c = 0 
data = file.readlines()
cdata = []
for i in data:
    if i.rstrip('\n') == types[0]:
        if len(types) == 1:
            break
        i1 = data.index(i)
        i2 = data.index(types[1]+'\n')
        cdata.append(data[i1+1: i2])
        types.pop(0)
cdata.append(data[i2+1: len(data)])
for i in range(len(cdata)):
    for j in range(len(cdata[i])):
        cdata[i][j] = cdata[i][j].rstrip('\n')
        cdata[i][j] = cdata[i][j].split(' ')
    cdata[i].pop(len(cdata[i])-1)
# # print(cdata)
cons = [[],[],[],[],[],[],[]]
k = 0
while k != 7:
    # print(k)
    c = cdata[k]
    c.sort(key=lambda x: int(x[0]))
    for i in c:
        p0 = int(i[0])
        p1 = int(i[1])
        p2 = int(i[2])
        cons[k].append([range(p0, p0+p2), range(p1, p1+p2)])
    k+=1

sd = []
nf = []
z = 0
while z != 7:
    sd = []
    for i in seeds:
        flag = True
        for j in cons[z]:
            if int(i) in j[1]:
                ind = j[1].index(int(i))
                sd.append(j[0][ind])
                flag = False
            else:
                nf.append(int(i))
        if flag:
            sd.append(i)
    z+=1
    seeds = sd

print(min(sd), seeds)
# seeds = sd
# sd = []
# z+=1
# for i in seeds:
#     flag = True
#     for j in cons[z]:
#         print(j)
#         break
#         if int(i) in j[1]:
#             ind = j[1].index(int(i))
#             sd.append(j[0][ind])
#             flag = False
#                 # print(nf)
#     if flag:
#         sd.append(i)

print(len(sd), len(seeds))
seeds = sd
z+=1
# for i in cons:
#     print("\n\n")
#     for j in i:
#         print(j)
