T = int(input())
def calc(index, c, point):
    answer.add(point)
    if index == len(d):
        return
        
    if c+d[index][0] <= L:
        calc(index+1, c+d[index][0], point+d[index][1])
    calc(index+1, c, point)

for i in range(T):
    N, L = map(int, input().split())
    
    d = []
    answer = set()
    for j in range(N):
        T, K = map(int, input().split())
        
        d.append([K, T])
    
    visited = set()
    calc(0, 0, 0)
    print(f"#{i+1} {max(answer)}")