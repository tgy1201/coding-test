T = int(input())

for i in range(T):
    N = int(input())
    
    li = []
    for j in range(N):
        e = input()
        ll = []
        for k in e:
            ll.append(int(k))
        li.append(ll)
    
    answer = sum(li[N//2])
    cnt = 1
    
    for j in range(1, N//2+1):
        answer += sum(li[N//2-j][cnt:N-cnt])
        answer += sum(li[N//2+j][cnt:N-cnt])
        cnt += 1
    print(f"#{i+1} {answer}")