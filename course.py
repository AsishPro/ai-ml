class Solution(object):
    def dfs(self,i,m,v):
        v[i]=1
        print(i)
        for k in m[i]:
            if v[k]==1:
                return False
            elif v[k]==0:
                # if true it will return directly without checking other nodes for loop so using if condition to traverse other neighbours too
                if not self.dfs(k,m,v):
                    return False
        v[i]=2   #only change here to for dfs.
        return True

    def canFinish(self, numCourses, prerequisites):
        print(prerequisites)
        m = [[] for _ in range(numCourses)]
        for i in prerequisites:
            m[i[0]].append(i[1])  #given directed graph so 
        print(m)
        v=[0 for i in range(numCourses)]
        for i in range(numCourses):
            t=self.dfs(i,m,v)
            print(t)
            if not t:
               return False
        return True
            
#https://leetcode.com/problems/course-schedule/submissions/1019115435/
            