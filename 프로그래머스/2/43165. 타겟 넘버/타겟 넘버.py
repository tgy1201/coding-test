def solution(numbers, target):   
    t = 0
    test = []
    def dfs(num, total):
        cnt = 0

        if num == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        
        for i in range(2):
            if i == 0:
                cnt += dfs(num+1, total + numbers[num])
            else:
                cnt += dfs(num+1, total - numbers[num])
        return cnt
    return dfs(0, t)