def solution(m, musicinfos):
    answer = ''
    m = calMusic(m)
    mx = -1
    
    for i in musicinfos:
        stime, etime, title, music = map(str, i.split(","))
        time = calTime(etime) - calTime(stime)
        
        music = calMusic(music)

        if(len(music) > time):
            music = music[:time]
        else:
            x = time // len(music)
            y = time % len(music)
            music = music * x + music[:y]
        
        if(m in music and time > mx):
            answer = title
            mx = time
    if(answer == ""):
        return "(None)"
    return answer

def calTime(time):
    a, b = map(int, time.split(":"))
    return a*60 + b

def calMusic(music):
    s = []
    for j in range(0, len(music)):
        if(music[j] == "#"):
            continue
        if(j == len(music) - 1):
            s.append(music[j])
            break
        if(music[j+1] == "#"):
            s.append(music[j].lower())
        else:
            s.append(music[j])
    return ''.join(s)