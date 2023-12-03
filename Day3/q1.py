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
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
                elif j == len(p)-1:
                    if data[i+1][j] in symbols:
                        flag.append(True)
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
                else:
                    if data[i+1][j] in symbols:
                        flag.append(True)
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
            elif i == len(data) - 1:
                if j == 0:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
                elif j == len(p)-1:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
                else:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
            else:
                if j == 0:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
                elif j == len(p)-1:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
                else:
                    if data[i-1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j+1] in symbols:
                        flag.append(True)
                    elif data[i][j+1] in symbols:
                        flag.append(True)
                    elif data[i+1][j+1] in symbols:
                        flag.append(True)
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j] in symbols:
                        flag.append(True)
                    elif data[i-1][j-1] in symbols:
                        flag.append(True)
                    elif data[i][j-1] in symbols:
                        flag.append(True)
                    elif data[i+1][j] in symbols:
                        flag.append(True)
                    elif data[i+1][j-1] in symbols:
                        flag.append(True)
                    else:
                        flag.append(False)
        else:
            if True in flag:
                part_nums.append(int(tpn))
            tpn = ''
            flag = []
print(sum(part_nums))