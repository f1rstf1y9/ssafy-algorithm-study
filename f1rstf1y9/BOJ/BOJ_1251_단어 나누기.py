word = input()
l = len(word)
ans = 'z'*l
for i in range(l-2):
    cur = ''
    for j in range(i+1, l-1):
        cur = word[i::-1] + word[j:i:-1] + word[l:j:-1]
        if ans > cur:
            ans = cur
print(ans)