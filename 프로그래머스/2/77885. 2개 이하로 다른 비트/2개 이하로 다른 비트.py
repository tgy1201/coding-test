def solution(numbers):
    answer = []

    for i in numbers:
        a = list(bin(i)[2:])
        a.insert(0, "0")

        check = 0
        for j in range(len(a) - 1, -1, -1):
            if a[j] == "1":
                check += 1
            else:  # '0'을 만난 경우
                if check < 1:  # 1이 하나 이하인 경우
                    a[j] = "1"
                    break
                else:  # 연속된 1이 2개 이상인 경우
                    a[j] = "1"
                    a[j + 1] = "0"
                    break

        num = int("".join(a), 2)  # 리스트 → 문자열 → 정수 변환
        answer.append(num)

    return answer