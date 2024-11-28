#Job5
for n in range(1000):
    if n <= 1:
        continue
    nbr = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            nbr = False
            break
    if nbr:
        print(n)
