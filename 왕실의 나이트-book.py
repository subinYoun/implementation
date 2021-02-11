a = input()
step = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
row = int(a[1])
column = int(ord(a[0]))-int(ord('a'))+1
result = 0
for i in step:
    next_row = row+i[0]
    next_column = column+i[1]
    if (1 <= next_row <= 8) and (1 <= next_column <= 8):
        result += 1
print(result)