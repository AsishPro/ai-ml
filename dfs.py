 
def dfs(ans,edges,n):
    v[n]=1
    ans.append(n)
    for i in edges[n]:
        if v[i]==0:
            dfs(ans,edges,i)   
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
edges=[[] for _ in range(n)]
for i in e:
    edges[i[0]].append(i[1])

ans=[]

v=[0 for i in range(n)]
print(edges)
for i in range(n):     #loop taken because to check disconnected components
    if not v[i]:
        dfs(ans,edges,i)
print(ans)




        