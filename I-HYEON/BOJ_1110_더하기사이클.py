N = int(input())
num = N
count = 0

while True:
        next = (num // 10) + num % 10
        num = (num % 10)*10 + next % 10
        count += 1
        if num == N:
            break

print(count)