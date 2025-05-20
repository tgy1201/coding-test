def dfs(index, s):
    if index == N:
        answer.append(s)
        return
    
    dfs(index+1, s)
    
    if s+li[index] <= K:
        dfs(index+1, s+li[index])
        
T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    
    li = list(map(int, input().split()))
    
    answer = []
    
    dfs(0, 0)
    
    print(f"#{i+1} {answer.count(K)}")