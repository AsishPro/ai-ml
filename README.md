# ai
codes done in ai course 
roll AP21110011239
cse N P. Asish Manoj Reddy


## week 1 
1. bfs - traverse nodes each level wise(after one level then next level), mark as visited. uses queue datastructure to remember next neighbouring node.
2. dfs - traverse in lift wize(top to bottom). here it can be used for detecting cycles which gives rise to topological sort
topological_sort using dfs - topological sort (where each node which is completed processing is stored) in dfs instead of visited. 
after visited each neighbouring node and loop completed it is marked completed or added to completed list to avoid further processing. (uses stack)
3. topological_sort using bfs - also called kahn's algorithm with modification to bfs in which, in queue 0 indegree node is added instead of each level nodes. after adding to queue, node removed from graph(indegrees of others reduced) . 
This gives linear ordering of how each node is traversed.
4. Question of which Course solved first - done using dfs(easy to detect cycle by processing each node) - toposort.
   https://leetcode.com/problems/course-schedule/submissions/1019115435/ - submission 

Remember point - Topological sort done on directed acyclic graph. - because in cycling graph there is no order(loop). so topo sort is used to detect cycles.


## Statespace
* given a puzzle/matrix with one index as empty(-1) find all combinations possible according to given level
2. with heuristic:
* class is declared which stores the matrix,parent id,heuristic. indexing done using id.
