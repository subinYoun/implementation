n = int(input())
t = n
r = 100
m = 0
while True:
    r = (((t//10)+(t % 10)) % 10)+((t % 10)*10)
    t = r
    m += 1
    if r == n:
        break
print(m)