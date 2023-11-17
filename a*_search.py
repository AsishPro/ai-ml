import heapq
import numpy as np

class state:
    def __init__(self, m,parent,l):
        global id
        self.id = id
        self.m = m
        self.parent = parent
        self.h = heuristic(m)
        self.l = l

def heuristic(m):
    t=np.array([[1,2,3],[4,5,6],[7,8,-1]])
    dis=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            r1,r2 = np.where(t == m[i][j])
            a,b = r1[0],r2[0]
            dis +=abs(i-a)+abs(j-b)
    return dis

def swapv(x, y, c, m2):
    m3 = np.copy(m2)
    m3[x][c],m3[y][c] = m3[y][c],m3[x][c]
    return m3

def swaph(x,y,c,m2):
    m3 = np.copy(m2)
    m3[c][x],m3[c][y]=m3[c][y],m3[c][x]
    return m3

def find(temp):
    for i in objects.values():
        if np.array_equal(i.m, temp):
            return True
    return False

def Create(m2, i, l):
    global id
    i1, i2 = np.where(m2 == -1)
    a, b = i1[0], i2[0]

    if objects[id].h == 0:
        return id

    if i>l:
        return None
    
    pq = []
    parent= objects[id].id
    if a-1>=0:
        t = swapv(a - 1, a, b, m2)
        if not find(t):
            heapq.heappush(pq,(heuristic(t), tuple(map(tuple,t))))
    if a+1<r:
        t = swapv(a + 1, a, b, m2)
        if not find(t):
            heapq.heappush(pq,(heuristic(t), tuple(map(tuple,t))))
    if b-1>=0:
        t = swaph(b - 1, b, a, m2)
        if not find(t):
            heapq.heappush(pq,(heuristic(t), tuple(map(tuple,t))))
    if b+1<c:
        t = swaph(b + 1, b, a, m2)
        if not find(t):
            heapq.heappush(pq,(heuristic(t), tuple(map(tuple,t))))

    while pq:
        st = np.array(heapq.heappop(pq)[1])
        id += 1
        objects[id] = state(st, parent, i)
        result = Create(st, i + 1, l)
        if result is not None:
            return result
        
    return None

def print_solution(result):
    res = [] 

    current = result
    while current!= 0:
        res.append(current)
        current = objects[current].parent   

    res.reverse()


    for state_id in res:
        current = objects[state_id]
        print("State ID:", current.id)
        print("Matrix:")
        print(f"{current.m}\nheuristic :{current.h}\nlevel:{current.l}")
        print("-----")
        print()



def matrix_input():
    m = []
    r = int(input("number of rows of matrix: "))
    c = int(input("number of columns: "))
    for i in range(r):
        temp = input(f"Enter row {i + 1} with spaces: ").split()
        m.append([int(x) for x in temp])
    return np.array(m)

# Input puzzle matrix
# m = matrix_input()

m = np.array([[1, 2, 3], [4, 5, -1], [6,7,8]])
id = 0
level = int(input("Enter until level: "))

objects = {}
level_map = {}

objects[id] = state(m, -1, 0)
l = level

# Rows and columns
r = m.shape[0]
c = m.shape[1]
result = Create(m, 1, l)

if result is not None:
    print("Solution found with ID:", result)
    print("Printing Solution Sequence:")
    print_solution(result)
else:
    print("No solution found.")

     

for obj in objects.values():
    level = obj.l
    if level not in level_map:
        level_map[level] = []
    level_map[level].append(obj)

# # # Print objects level-wise
# for i in level_map:
#     print()
#     print(f"level {i}")
#     for t in level_map[i]:
#         print(f"{t.m} - h(x) - {t.h}, parent = {t.parent}, {t.h}")
