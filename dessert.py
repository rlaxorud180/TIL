import sys
sys.stdin=open("input.txt")
from pprint import pprint
from collections import deque


t=int(input())


def dfs(s, x, y, visited, cnt):
    global start_x, start_y, ans
    if s > 3:
        return

    if s == 3 and x == start_x and y == start_y and ans < cnt:
        ans = cnt
        return

    for k in range(s,s+2):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n and visited[a[nx][ny]]==0:
            visited[a[nx][ny]]=1
            dfs(k,nx,ny,visited,cnt+1)
            visited[a[nx][ny]]=0

for tc in range(1,1+t):

    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans=-1
    dx=[1,1,-1,-1,0]
    dy=[-1,1,1,-1,0]

    for i in range(n-2):
        for j in range(1,n-1):
            start_x=i
            start_y=j
            v=[0]*101
            dfs(0,i,j,v,0)
    print(f"#{tc} {ans}")
