from cs50 import get_float

while True:
    owed = get_float("Change owed: ")
    if owed >= 0:
        break

owed *= 100

coins = owed // 25
owed %= 25
coins += owed // 10
owed %= 10
coins += owed // 5
owed %= 5
coins += owed

print(int(coins))
