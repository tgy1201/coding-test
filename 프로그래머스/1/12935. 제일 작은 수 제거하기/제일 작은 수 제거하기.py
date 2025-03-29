def solution(arr):
    if(len(arr) <= 1):
        return list([-1])
    arr.remove(min(arr))
    return arr