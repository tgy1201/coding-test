def solution(brown, yellow):
    answer = []
    cnt = 1
    while True:
        if yellow % cnt !=0:
            cnt+= 1
            continue
        row = yellow // cnt
        col = cnt
        
        if (col+2)*2 + row*2 == brown:
            return [row+2, col+2]
        cnt +=1