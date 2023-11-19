import numpy as np

#for storing state
class state:
    def __init__(self,m,parent,l):
        global id
        id+=1
        self.id=id
        self.m=m
        self.parent=parent
        self.h=heuristic(m) 
        self.l=l

    
def heuristic(m):
    t=np.array([[1,2,3],[4,5,6],[7,8,-1]])
    c=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if not m[i][j]==t[i][j]:
                c+=1
    return c

#swap vertical - 2nd dimension same
#swap horizontal - 1st dimension same
def swapv(x,y,c,m2):
    m3=np.copy(m2)
    m3[x][c],m3[y][c]=m3[y][c],m3[x][c]
    return m3
def swaph(x,y,c,m2):
    m3=np.copy(m2)
    m3[c][x],m3[c][y]=m3[c][y],m3[c][x]
    return m3


def Create(m2,i,l):
    if i>l:                  #reached level exit
        return 0    
    
    i1,i2=np.where(m2==-1)   #finding -1 location
    a,b=i1[0],i2[0]  

    #explore all 4 sides if exist and add state.
    parent=objects[id].id
    print(id)
    if a-1>=0: 
        t=swapv(a-1,a,b,m2)
        objects[id]=state(t,parent,i)
        Create(t,i+1,l)
    if a+1<r:
        t=swapv(a+1,a,b,m2)
        objects[id]=state(t,parent,i)
        Create(t,i+1,l)
    if b-1>=0:
        t=swaph(b-1,b,a,m2)
        objects[id]=state(t,parent,i)
        Create(t,i+1,l)
    if b+1<c :
        t=swaph(b+1,b,a,m2)
        objects[id]=state(t,parent,i)
        Create(t,i+1,l)

def matrix_input():
    m=[]
    r=int(input("number of rows of matrix: "))
    c=int(input("number of columns: "))
    for i in range(r):    
        temp=input(f"Enter row {i+1} with   spaces: ").split()
        m.append([int(x) for x in temp])
    return np.array(m)

#for custom input
# m=matrix_input()
m=np.array([[1,8,3],[5,7,4],[6,2,-1]])
id=0
l=int(input("enter until level: "))

objects={}  #map of objects with indexing as id for tracing back the path
level_map={} # for indexing level wise


objects[id]=state(m,-1,0)
#id=1 here
# print(objects[1].m)

#rows and columns
print(m.shape)
r=m.shape[0]
c=m.shape[1]
Create(m,1,l) 


# # print("this states")
# for i in objects:
#     print(objects[i].m)

for obj in objects.values():
    level = obj.l
    if level not in level_map:
        level_map[level] = []
    level_map[level].append(obj)

# Print objects level-wise
for i in level_map:
    print()
    print(f"level {i}")
    for t in level_map[i]:
        print(f"{t.m} - h(x) - {t.h}, parent = {t.parent} ,id = {t.id}")

#the parent id's are different from level as this is similar to dfs
#can also index the objects using id(objects map).
