import os
file = open('Day1/input.txt', 'r')
data = file.readlines()
nd = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}

if __name__ == '__main__':
    num = []
    for i in data:
        temp = []
        for j in range(len(i)):
            t = ''
            for k in range(j,len(i)):
                t += i[k]
                if t in nd.keys():
                    temp.append(nd[t])
                else:
                    try:
                        a = int(t)
                        temp.append(t)
                    except:
                        pass
        if len(temp)<2:
            num.append(int(temp[0]+temp[0]))
        elif len(temp)>2:
            num.append(int(temp[0]+temp[len(temp)-1]))
        else:
            num.append(int(temp[0]+temp[1]))
    print(sum(num))