dd = ['Fizz', 'Buzz', 'FizzBuzz']

n = 0
current = 0
for i in range(3):
    s = input()

    if s not in dd:
        current = int(s)
        n = i

current = current + (3-n)

if current % 15 == 0:
    print("FizzBuzz")
elif current % 3 == 0 and current % 5 != 0:
    print("Fizz")
elif current % 3 != 0 and current % 5 == 0:
    print("Buzz")
else:
    print(current)