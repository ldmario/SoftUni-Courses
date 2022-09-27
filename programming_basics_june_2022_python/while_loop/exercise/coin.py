money = float(input())
money = int(money * 100)
coins = 0

while True:
    if money >= 2 * 100:
        coins += money // (2 * 100)
        money %= (2 * 100)
    elif money >= 1 * 100:
        coins += money // (1 * 100)
        money %= (1.00 * 100)
    elif money >= 0.50 * 100:
        coins += money // (0.50 * 100)
        money %= (0.50 * 100)
    elif money >= 0.20 * 100:
        coins += money // (0.2 * 100)
        money %= (0.20 * 100)
    elif money >= 0.10 * 100:
        coins += money // (0.1 * 100)
        money %= (0.1 * 100)
    elif money >= 0.05 * 100:
        coins += money // (0.05 * 100)
        money %= (0.05 * 100)
    elif money >= 0.02 * 100:
        coins += money // (0.02 * 100)
        money %= (0.02 * 100)
    elif money >= 0.01 * 100:
        coins += money // (0.01 * 100)
        money %= (0.01 * 100)
    elif money == 0:
        break

print(int(coins))
