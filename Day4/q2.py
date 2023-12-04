file = open('Day4/input.txt', 'r')
file2 = open('Day4/test.txt', 'w')
data = file.readlines()
for i in range(len(data)):
    data[i] = data[i].rstrip('\n')

# data = data[:13]
# print(data)
print(len(data))
og = 1
c = 0
t = 2
# print(c)
buff = []

def solve(arr):
    ret = []
    for i in range(len(arr)):
        temp = arr[i]
        temp = temp.split(":")
        temp.pop(0)
        temp = temp[0].split('|')
        cnums = temp[0].rstrip(' ').lstrip(' ').split(" ")
        nums = temp[1].rstrip(' ').lstrip(' ').split(" ")
        # print(cnums, nums)
        p = data.index(arr[i])
        for j in cnums:
            try:
                t = int(j)
                if j in nums:
                    p+=1
                    ret.append(data[p])
            except:
                pass
    return ret
ans = len(data)
c = 0
def writer(d):
    for i in range(len(d)):
        file2.writelines(d[i])
        file2.write('\n')
    file2.write('\n')
    file2.write('\n')

tren = [data]
lent = []
while c != 100:
    tren.append(solve(tren[c]))
    # print(tren[c])
    # writer(tren[c])
    lent.append(len(tren[c]))
    # s2 = solve(s1[:1])
    # s3 = solve(s2[:1])
    # print(s3)
    c+=1
print(sum(lent)) 
print(lent)
    
# print(len(data))
# print(data[18])
# file2.writelines(data)
