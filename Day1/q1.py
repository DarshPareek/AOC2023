import os
file = open('Day1/input.txt', 'r')
data = file.readlines()
if __name__ == '__main__':
    num = []
    for i in data:
        temp = []
        for j in i:
            try:
                a = int(j)
                temp.append(j)
            except:
                pass
        if len(temp)<2:
            num.append(int(temp[0]+temp[0]))
        elif len(temp)>2:
            num.append(int(temp[0]+temp[len(temp)-1]))
        else:
            num.append(int(temp[0]+temp[1]))
    print(len(num))