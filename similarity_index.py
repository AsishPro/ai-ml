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
f=open('t2.txt','r')
ch=0
l=0
for i in f:
    l+=1
    ch+=find(i,w1)
print(f"characters: {ch}\nlines: {l}\nwords: {len(w1)}")
print(w1)

w2=[]
f=open('text.txt','r')
ch=0
l=0
for i in f:
    l+=1
    ch+=find(i,w2)
print(f"characters: {ch}\nlines: {l}\nwords: {len(w2)}")
print(w2)

common=0
for i in w1:
    if i in set(w2):
        common+=1

print(common)
print(f"similaity index:{common/(len(w1)+len(w2))}")


