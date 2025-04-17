t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    half = m // 2
    l_prime = max(l, -half)
    r_prime = l_prime + m
    if r_prime > r:
        r_prime = r
        l_prime = r_prime - m
    print(l_prime, r_prime)



