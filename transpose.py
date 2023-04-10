m,n=map(int,input().split())
matrix = []
for i in range(m):
  row=list(map(int,input().split()))
  matrix.append(row)
transpose=[[matrix[j][i]for j in range (m)]for i in range(n)]
for row in transpose:
  print(*row)