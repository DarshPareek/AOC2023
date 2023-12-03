file = open('Day3/input.txt', 'r')
# data = file.read()
symbols = {'', '+', '/', '-', '%', '@', '*', '#', '$', '=', '&'}
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# for i in data:
#     if i != '.' and i not in nums:
#         symbols.add(i.strip('\n'))
# print(symbols)
data = file.readlines()
part_nums = []
part_pos = []
gear = 0
gear_ratios = []
for i,p in enumerate(data):
    tpn = ''
    flag = []
    for j,q in enumerate(p):
        if q in nums:
            tpn += q
            if i == 0:
                if j == 0:
                    if data[i+1][j] in symbols:
                        flag.append(True)
                        gear = ((i+1, j, data[i+1][j]))
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j+1, data[i+1][j+1]))
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                        gear = ((i, j+1, data[i][j+1]))
                    else:
                        flag.append(False)
                elif j == len(p)-1:
                    if data[i+1][j] in symbols:
                        flag.append(True)
                        gear = ((i+1, j, data[i+1][j]))
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j-1, data[i+1][j-1]))
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                        gear = ((i, j-1, data[i][j-1]))
                    else:
                        flag.append(False)
                else:
                    if data[i+1][j] in symbols:
                        flag.append(True)
                        gear = ((i+1, j, data[i+1][j]))
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j+1, data[i+1][j+1]))
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                        gear = ((i, j+1, data[i][j+1]))
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j-1, data[i+1][j-1]))
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                        gear = ((i, j-1, data[i][j-1]))
                    else:
                        flag.append(False)
            elif i == len(data) - 1:
                if j == 0:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                        gear = ((i-1, j, data[i-1][j]))
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j+1, data[i-1][j+1]))
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                        gear = ((i, j+1, data[i][j+1]))
                    else:
                        flag.append(False)
                elif j == len(p)-1:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                        gear = ((i-1, j, data[i-1][j]))
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j-1, data[i-1][j-1]))
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                        gear = ((i, j-1, data[i][j-1]))
                    else:
                        flag.append(False)
                else:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                        gear = ((i-1, j, data[i-1][j]))
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j+1, data[i-1][j+1]))
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                        gear = ((i, j+1, data[i][j+1]))
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j-1, data[i-1][j-1]))
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                        gear = ((i, j-1, data[i][j-1]))
                    else:
                        flag.append(False)
            else:
                if j == 0:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                        gear = ((i-1, j, data[i-1][j]))
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j+1, data[i-1][j+1]))
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                        gear = ((i, j+1, data[i][j+1]))
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j+1, data[i+1][j+1]))
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                        gear = ((i+1, j, data[i+1][j]))
                    else:
                        flag.append(False)
                elif j == len(p)-1:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                        gear = ((i-1, j, data[i-1][j]))
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j-1, data[i-1][j-1]))
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                        gear = ((i, j-1, data[i][j-1]))
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                        gear = ((i+1, j, data[i+1][j]))
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j-1, data[i+1][j-1]))
                    else:
                        flag.append(False)
                else:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                        gear = ((i-1, j, data[i-1][j]))
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j+1, data[i-1][j+1]))
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                        gear = ((i, j+1, data[i][j+1]))
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j+1, data[i+1][j+1]))
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                        gear = ((i+1, j, data[i+1][j]))
                    elif data[i-1][j] in symbols:
                        flag.append(True)
                        # gear = ((i-1, j, data[i-1][j]))
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i-1, j-1, data[i-1][j-1]))
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                        gear = ((i, j-1, data[i][j-1]))
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                        # gear = ((i+1, j, data[i+1][j]))
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                        gear = ((i+1, j-1, data[i+1][j-1]))
                    else:
                        flag.append(False)
        else:
            if True in flag:
                part_nums.append(int(tpn))
                part_pos.append(gear)
            tpn = ''
            flag = []
# print(part_nums[:20])
# print(part_pos[:20])
used = []
for i in part_pos:
    ind = []
    for j in range(len(part_pos)):
        if i == part_pos[j] and i[2] == '*' and j not in used:
            # print(True)
            ind.append(j)
            used.append(j)
    if len(ind) == 2:
        n1 = part_nums[ind[0]]
        n2 = part_nums[ind[1]]
        # if n1 not in used and n2 not in used:
        gear_ratios.append(n1*n2)

print(sum(gear_ratios))