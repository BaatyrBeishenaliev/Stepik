n = int(input())
k = input().lower()
sp = []

for _ in range(n):
    s = input().lower()

    if k.lower() in s.lower():
        sp.append(s)

print(sp)