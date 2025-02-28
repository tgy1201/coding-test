from collections import deque
def solution(n):
    queue = deque()
    answer = 1
    if(n == 2 or n ==1):
        return 1
    
    for i in range(n//2+1, 0, -1):
        queue.append(i)
        s = sum(queue)
        if(s > n):
            queue.popleft()
        elif(s == n):
            answer +=1
        
    return answer

'''
1 : 1
2 : 2
3 : 12 3
4 : 4
5: 23 5
6: 123 6
7: 34 7
8: 8
9: 234 45 9
10: 1234 10
11: 56 11
'''