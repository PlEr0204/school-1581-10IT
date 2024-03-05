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
print("10 класс:")
k=0
print(ans)

for i in range(len(ans)):
    t = ans[i]
    j = i - 1
    while j >= 0 and t.score > ans[j].score:
        ans[j+1] = ans[j]
        j -= 1
    ans[j+1] = t
for i in range(1,len(start)):
    if ans[i].clas[:-1] == "10":
        k += 1
        print(k, "место", ans[i].name)
    if k == 3:
        break