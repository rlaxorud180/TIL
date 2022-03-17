
def makeTree(n):
  global count
  # 배열이니까 배열크기 넘어가지 않도록
  if n <= N :

    makeTree(n*2)
    tree[n] = count

    count += 1


    makeTree(n*2+1)


N=15
tree=[0 for i in range(N+1)]
count=1

makeTree(1)
print(tree)
