m, n = map(int, input().split())
ƯCLN  = 1
for i in range(1, min(m, n)+1):
    if m % i == 0 and n % i == 0:
        ƯCLN  = i
BCNN  = m * n // ƯCLN 
print("UCLN:", ƯCLN )
print("BCNN:", BCNN )
