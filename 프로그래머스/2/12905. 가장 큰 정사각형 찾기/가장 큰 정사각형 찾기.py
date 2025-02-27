def solution(board):
    answer = 0
    dp=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    # 첫열과 행을 미리 셋팅하는 부분
    dp[0] = board[0]
    for row in range(len(board)):
        dp[row][0] = board[row][0]

    for row in range(0,len(dp)):
        for col in range(0,len(dp[0])):
        	# 첫열과 첫행 부분은 넘기며, 현재 블록 값이 1인 경우에만 계산
            if (row - 1 >= 0) and (col -1 >= 0) and board[row][col] ==1:
            	
                dp[row][col] = min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1

    for i in range(len(dp)):
        temp = max(dp[i])
        answer = max(answer, temp)


    return answer*answer
'''
#효율성 실패
from collections import deque, Counter
import copy

def solution(board):
    queue = deque()
    hx = [0, 1, 1]
    hy = [1, 0, 1]
    dd = []
    answer = 0
    
    for a in range(len(board)):
        for b in range(len(board[0])):
            if(board[a][b] == 1):
                cboard = copy.deepcopy(board)
                dd = []
                queue.append((a,b,1))
                dd.append(1)

                while queue:
                    x, y, depth = queue.popleft()
                    for i in range(3):
                        dx = x + hx[i]
                        dy = y + hy[i]

                        if dx >= len(cboard) or dy >= len(cboard[0]):
                            break
                        if cboard[dx][dy] == 0:
                            break
                        if cboard[dx][dy] == 1:
                            cboard[dx][dy] = 2
                            queue.append((dx, dy, depth+1))
                            dd.append(depth+1)

                cc = Counter(dd)
                cnt = 0
                mm = 0
                for i in cc.keys():
                    cnt += cc[i]
                    if(int(i)**2 == cnt):
                        mm = i
                if answer < mm ** 2:
                    answer = mm **2

    return answer
'''