ruangan = int(input())
jumlah  = []
zetsu   = list(map(int, input().split()))
print()
for i in range(ruangan):
    print((i+1)*zetsu[i], end=' ')