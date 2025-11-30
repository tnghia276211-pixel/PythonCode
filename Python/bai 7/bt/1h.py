from collections import Counter
A = list(map(int, input().split()))
dem = Counter(A)
for x in A:
    if dem[x] == 1:
        print(x, end=" ")
