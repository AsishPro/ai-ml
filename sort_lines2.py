
#find function converts line to list of words and sorts 
#removing "." and "\n"
def find(words):
    lt=[' ','.','\n']
    res=[]
    temp=""
    for j in range(len(words)):
        if (i[j]==' ') or (i[j]=='.'):
          res.append(temp)
          temp=""
        if i[j] not in lt:
            temp+=i[j]
    if temp!="":
        res.append(temp) 
    res=[t.lower() for t in res]
    res=sorted(res)
    if words[-2]=='.' or words[-1]=='.':
        res.append('.')
    return res

#read file
lt=[]
f=open("t2.txt",'r')
l=0

#iterate line by line in f
for i in f:
    l+=1
    lt.append(find(i))
f.close()

#sort lines again
lt.sort()
#opening new file in write
f=open('t3.txt','w')

for i in lt:
    t=" ".join(i)
    f.write(t+'\n')
f.close()