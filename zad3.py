class Studentiki:
    pass
f = open("students.csv", encoding="utf8")
start = []
f.readline()
for i in f:
    start.append(i[:-1])
print(start)
ans = []

j1=0
for i in range(len(start)):
    ans.append(Studentiki())
    s = start[i].split(",")
    ans[j1].idd = s[0]
    ans[j1].name = s[1]
    ans[j1].tidd = s[2]
    ans[j1].clas = s[3]
    if s[4] == "None":
        s[4] = '0'
    ans[j1].score = s[4]
    j1+=1
for i in range(len(start)):
    n = input()
    while n != 'СТОП':
        if int(n) > 500:
            print('Ничего не найдено')
            break
        else:
            d=int(n)
            print('Проект №', (d),'делал:', start[d+1].name, 'он(а) получил(а) оценку -', start[d+1].score)
            x=input()
    if n=='СТОП':
        break