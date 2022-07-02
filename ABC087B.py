kaisuu500 = int(input())
kaisuu100 = int(input())
kaisuu50 = int(input())
kingaku = int(input())
count = 0

for a in range(kaisuu500+1):
    for b in range(kaisuu100+1):
        for c in range(kaisuu50+1):
            if 500 * a + 100 * b + 50 * c ==kingaku:
                count += 1
print(count)