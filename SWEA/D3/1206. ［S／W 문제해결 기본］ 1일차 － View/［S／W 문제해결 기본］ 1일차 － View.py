for i in range(10):
    N = int(input())

    h = list(map(int, input().split()))
    answer = 0
    for j in range(2, len(h)-2):
        m = max(h[j-2],h[j-1],h[j+1],h[j+2])
        
        if m < h[j]:
            answer += h[j] - m
    print(f"#{i+1} {answer}")