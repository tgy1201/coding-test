def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: x)
    
    for i in range(0, len(phone_book)-1):
        try:
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
        except:
            continue
    return True