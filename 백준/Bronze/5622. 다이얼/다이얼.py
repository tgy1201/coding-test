a = input()
count = 0
b = {2: ['A','B','C'], 3: ['D','E','F'], 4: ['G','H','I'], 5: ['J','K','L'], 6: ['M','N','O'], 7: ['P','Q','R','S'], 8: ['T','U','V'], 9: ['W','X','Y','Z']}

for i in range(len(a)):
    for j in range(2,10):
        if a[i] in b[j]:
            count += j

print(count+len(a))