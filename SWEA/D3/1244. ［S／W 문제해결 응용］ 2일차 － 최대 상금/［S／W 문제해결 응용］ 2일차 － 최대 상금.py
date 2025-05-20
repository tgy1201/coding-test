C = int(input())

def exchange(li, cnt):
    if cnt == E:
        aa.add(int(''.join(li)))
        return
    for i in range(len(li)):
        for j in range(i+1, len(li)):  # 중복 줄이기
            li[i], li[j] = li[j], li[i]
            a = ''.join(li)
            if (a, cnt) not in answer:
                answer.add((a, cnt))
                exchange(li[:], cnt+1)
            li[i], li[j] = li[j], li[i]
for i in range(C):
    N, E = map(int, input().split())
    
    li = []
    answer = set()
    aa = set()
    for j in str(N):
        li.append(j)
    exchange(li, 0)
    print(f"#{i+1} {max(aa)}")