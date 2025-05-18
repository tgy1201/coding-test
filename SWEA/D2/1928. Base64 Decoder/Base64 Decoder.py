T = int(input())

d = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/' ]
for i in range(T):
    buf = ""
    s = input()
    for j in s:
        jj = str(bin(d.index(j))[2:])
        if len(jj) < 6:
            jj = "0"*(6-len(jj)) + jj
        buf += jj    
    b = []
    for k in range(0, len(buf), 8):
        ee = int("0b"+buf[k:k+8],2)
        b.append(chr(ee))
    print(f"#{i+1} {''.join(b)}")