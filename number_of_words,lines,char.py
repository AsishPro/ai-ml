def find(i,words):
    c=0
    lt=[' ','.','\n']
    temp=""
    for j in range(len(i)):
        c+=1
        if (i[j]==' ') or (i[j]=='.'):
          words.append(temp)
          temp=""
        if i[j] not in lt:
            temp+=i[j]
    if temp!="":
        words.append(temp) 
    return c

w1=[]
#should be in directory outside this code
txt=input("Input file name:")
f=open(txt+".txt",'r')
ch=0
l=0
for i in f:
    l+=1
    ch+=find(i,w1)
print(f"characters: {ch}\nlines: {l}\nwords: {len(w1)}")
print(w1)
f.close()