def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for x in range(len(arr1)):
        for y in range(len(arr2[0])):
            for z in range(len(arr2)):
                answer[x][y] += arr1[x][z]*arr2[z][y]
    return answer
'''
14 0 n + 
32
41

3 3
3 3

232
424
314

543
241
311

'''