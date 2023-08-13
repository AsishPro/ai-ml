
def bfs(ans,edges,n):
    q=[]
    q.append(n)
    
    while not len(q)==0:
        t=q.pop(0)
        ans.append(t)
        v[t]=1
        for i in edges[t]:
                if v[i]==0:
                    q.append(i)
                    v[i]=1    #why because
    return ans


#custom input of edges
# n,m = map(int, input().split())  #m - edges
# edges=[[] for i in range(n)]     #empty dictionary/adjacency list
# for i in range(m):               #edges pairs are taken(unidirectional)
#     a,b=map(int,input().split())
#     edges[a].append(b)
#     edges[b].append(a)

n=6
e=[[1,2],[1,5],[2,5],[3,4],[2,3],[3,5],[5,4]]
edges=[[] for i in range(n)] 
for i in e:             
    edges[i[0]].append(i[1])
    edges[i[1]].append(i[0])

print(edges)
v=[0 for i in range(n)]
ans=[]

for i in range(n):     #loop taken because to check disconnected components
    if not v[i]:
        bfs(ans,edges,i)
print(ans) 


        
                








    



