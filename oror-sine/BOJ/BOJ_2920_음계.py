ascending = [i for i in range(1,9)]
chords = list(map(int, input().split()))

if chords == ascending:
    print("ascending")
elif chords == ascending[::-1]:
    print("descending")
else:
    print("mixed")