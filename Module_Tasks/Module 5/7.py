f1 = 1
f2 = 1

n = input()
n = int(n)

i = 0
while i < n - 2:
    f_sum = f1 + f2
    f1 = f2
    f2 = f_sum
    i = i + 1

print(f2)