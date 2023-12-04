file = open('Day4/input.txt', 'r')
data = file.readlines()
points = []
for i in range(len(data)):
    data[i] = data[i].rstrip('\n')
for i in range(len(data)):
    temp = data[i]
    temp = temp.split(":")
    temp.pop(0)
    temp = temp[0].split('|')
    cnums = temp[0].rstrip(' ').lstrip(' ').split(" ")
    nums = temp[1].rstrip(' ').lstrip(' ').split(" ")
    p = 0
    for i in cnums:
        try:
            t = int(i)
            if i in nums:
                if p == 0:
                    p+=1
                else:
                    p*=2
        except:
            pass
    points.append(p)
print((points))