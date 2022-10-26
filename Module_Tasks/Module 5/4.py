numb = []
endN = 1
count = 0

while True:
    num = int(input())
    endN = num
    numb.append(num)

    if endN == 0:
        break

i = 0
while i < len(numb) - 1:
    if numb[i] < numb[i + 1]:
        count += 1
    i += 1
print(count)