import numpy as np 

def dfs(ans,matrix,n):
    v[n]=1
    ans.append(n)
    for i in range(len(matrix[0])):
        if matrix[n][i]==1 and v[i]==0:
            dfs(ans,matrix,i)   
    return ans

def bfs(ans,matrix,n):
    q=[]
    q.append(n)
    
    while not len(q)==0:
        t=q.pop(0)
        ans.append(t)
        v[t]=1
        for i in range(len(matrix[0])):
                if matrix[t][i]==1 and v[i]==0:
                    q.append(i)
                    v[i]=1  
    return ans

def case3(matrix,n,e):
        #if matrix not created
        if len(matrix)==0:
            matrix=adj_matrix(n,e)

        #bfs using adj matrix
        for i in range(n):     #loop taken because to check disconnected components
            if not v[i]:
                bfs(ans1,matrix,i)
        print(f"bfs traversal: {ans1}")

def case4(matrix,n,e):
        #if matrix not created
        if len(matrix)==0:
            matrix=adj_matrix(n,e) 
        #dfs using adj matrix
        for i in range(n):    
            if not v[i]:
                dfs(ans2,matrix,i)
        print(f"dfs traversal: {ans2}")


def adj_matrix(n,e):
    matrix=np.array([[0 for i in range(n)] for j in range(n)])
    for i in e:             
        matrix[i[0]][i[1]]=1
        matrix[i[1]][i[0]]=1
    return matrix

def adj_list(n,e):
    adj=[[] for i in range(n)] 
    for i in e:             
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    return adj


# #Custom input for Graph start from 0 node
# n,m = map(int, input("Enter the nodes(N),Edges(M) :").split())  #n-nodes m - edges
# e=[]
# #edges input is taken
# for i in range(m):        
#     a,b=map(int,input().split())
#     e.append([a,b])
# print(e)

#adj matrix
matrix=[]
#results for bfs,dfs
ans1=[] 
ans2=[]

#predefined graph edges
n=5
e=[[0,1],[0,4],[1,4],[2,3],[1,2],[2,4],[4,3]]

case=int(input("Enter the Case:\n1.Adjacency Matrix\n2.Adjacency List\n3.BFS\n4.DFS\n5.BFS,DFS\n6.Exit\nInput: "))
while case!=6:    
    if case==1:    
        matrix=adj_matrix(n,e)

        #printing adjacency matrix
        print("adjacency matrix: ")
        t=[i for i in range(len(matrix))]
        print("   ",end="")
        print(*t)
        for i,j in enumerate(matrix):
            print(i,j)

    if case==2:
        adj=adj_list(n,e)
        print("adjacency list: ")
        for i,j in enumerate(adj):
            print(f"{i}- {j}")

    if case==3:
        v=[0]*n
        ans1=[]
        case3(matrix,n,e)

    if case==4:
        v=[0]*n
        ans2=[]
        case4(matrix,n,e)

    if case==5:
        #if bfs not already called
        if len(ans1)==0:
            v=[0]*n
            ans1=[]
            case3(matrix,n,e)   
        #if dfs not already called  
        if len(ans2)==0:
            v=[0]*n
            ans2=[]
            case4(matrix,n,e)
    if case==6:
        print("done")
        exit(0)

    case=int(input("\nInput: "))
