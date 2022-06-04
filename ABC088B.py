Alice = 0
Bob =0
N = int(input())
a = list(map(int,input().split()))
a = sorted(a, reverse=True)
for i in range(N):
    if i % 2 == 0:
        Alice = Alice + a[i]
    else:
        Bob = Bob + a[i]
c = Alice - Bob
print(c)