numb = []
endN = 1

max_count = 1
current_count = 1

while True:
    endN = int(input())
    numb.append(endN)

    if endN == 0:
        break

i = 1

while i < len(numb):
    if numb[i - 1] == numb[i]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        max_count = max(max_count, current_count)
        current_count = 1
    i += 1

print(max_count)