from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n in range(1, 9):
        break
j = n - 1
for i in range(1, n + 1):
    print(" " * j + "#" * i)
    j -= 1
