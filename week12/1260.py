import sys
input=sys.stdin.readline

def dfs(v,res):
    print(v,end=' ')
    for i in graph[v]:
        if i not in res:
            res.append(i)
            dfs(i,res)

def bfs():
    q = [v]
    result=[v]
    while q:
        now = q.pop(0)
        for i in graph[now]:
            if i not in result:
                result.append(i)
                q.append(i)
            continue
    print(*result)

n,m,v=map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort()

dfs(v, [v])
print()
bfs()