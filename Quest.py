f=open("17_13088.txt")
m=[]
ans=0
for i in range(6634):
    m.append(int(f.readline()))
chet=0
m1=[]
m2=[]
for j in range(len(m)):
    if m[j]%100==17:
        m1.append(m[j])
for i in range(len(m)-2):
    if len(str(m[i]))==4:
        chet+=1
    if len(str(m[i+1]))==4:
        chet+=1
    if len(str(m[i+2]))==4:
        chet+=1
    if chet==2:
        chet=0
        if m[i]%5==0 or m[i+1]%5==0 or m[i+2]%5==0:
            if m[i]+m[i+1]+m[i+2]>max(m1):
                m2.append(m[i]+m[i+1]+m[i+2])
                ans+=1
    else:
        chet=0
print(ans, max(m2))

