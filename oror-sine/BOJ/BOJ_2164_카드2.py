N = int(input())
cards = [i for i in range(1,N+1)]

while len(cards)>1:
    l = len(cards)
    cards = [e for i, e in enumerate(cards) if i%2]
    if l%2:
        down = cards.pop(0)
        cards.append(down)
        
print(cards[0])
