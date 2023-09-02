import numpy as np

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

    #explore all 4 sides if exist and add to level.
    if (a-1<r and a-1>=0): 
        t=swapv(a-1,a,b,m2)
        map[i].append(t)
        Create(t,i+1,l)
    if (a+1<r and a-1>=0):
        t=swapv(a+1,a,b,m2)
        map[i].append(t)
        Create(t,i+1,l)
    if (b-1<c and b-1>=0):
        t=swaph(b-1,b,a,m2)
        map[i].append(t)
        Create(t,i+1,l)
    if (b+1<c and b-1>=0):
        t=swaph(b+1,b,a,m2)
        map[i].append(t)
        Create(t,i+1,l)

def matrix_input():
    m=[]
    r=int(input("number of rows of matrix: "))
    c=int(input("number of columns: "))
    for i in range(r):    
        temp=input(f"Enter row {i+1} with spaces: ").split()
        m.append([int(x) for x in temp])
    return np.array(m)

#for custom input
# m=matrix_input()
m=np.array([[1,8,3],[5,7,4],[6,2,-1]])

level=int(input("enter until level: "))
map={i:[] for i in range(level+1)}

map[0].append(m) #base matrix at level 0

l=level
#rows and columns
print(m.shape)
r=m.shape[0]
c=m.shape[1]
Create(m,1,l)

#printing all combinations
for i in map:
    print()
    print(f"level {i}:")
    for j in map[i]:
        print(j)