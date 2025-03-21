def solution(triangle):
    answer = 0
    d = [[0] * (i+1) for i in range(len(triangle))]
    d[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j-1] + triangle[i][j], d[i-1][j] + triangle[i][j])
        
    return max(d[len(triangle)-1])