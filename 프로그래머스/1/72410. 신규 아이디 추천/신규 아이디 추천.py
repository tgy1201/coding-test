def solution(new_id):
    data = "abcdefghijklmnopqrstuvwxyz1234567890-_."
    #1
    new_id = new_id.lower()
    
    #2
    new_id = list(filter(lambda x: x in data, new_id))
    new_id = ''.join(new_id)
    
    if(len(new_id) == 0):
        new_id = "."
        
    #3
    cnt = 0
    data = new_id
    new_id = list(new_id)
    for i, v in enumerate(data):
        if(v == "."):
            cnt += 1
            
            if(cnt == 2):
                new_id[i] = ""
                cnt -= 1
        else:
            cnt = 0
            
    new_id = ''.join(new_id)
    
    #4
    if(new_id[0] == "."):
        new_id = new_id[1:]
    if(new_id[-1:] == "."):
        new_id = new_id[:-1]
    
    #5
    if(len(new_id) == 0):
        new_id = "a"
    
    #6
    if(len(new_id) >= 16):
        new_id = new_id[:15]
        if(new_id[-1:] == "."):
            new_id = new_id[:-1]
            
    #7
    if(len(new_id) <= 2):
        while(len(new_id) < 3):
            new_id += new_id[-1:]
    return new_id