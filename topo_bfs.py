# topo sort - linear ordering
#  if there is an edge between u,v. u appears before v in linear ordering.
# Algorithm Kahn's
#remove all 0 degree nodes and reduce connected degrees. append new 0 degree nodes. continue till last
 


n=6
e=[[1,2],[1,5],[2,5],[3,4],[2,3],[3,5],[5,4]]
edges=[[] for _ in range(n)]
degree=[0 for _ in range(n)]
for i in e:
    degree[i[1]]+=1
    edges[i[0]].append(i[1])

print(degree)


print(edges)
ans=[]

q=[]
for i in range(n):     
    if degree[i]==0:
         q.append(i)
# print(q)

while not len(q)==0:
     t=q.pop(0)
     ans.append(t)
     for i in edges[t]:
          degree[i]-=1
          if degree[i]==0:
               q.append(i)
print(ans) 


        
        