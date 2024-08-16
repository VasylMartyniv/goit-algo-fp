def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for item, info in items.items():
        for cost in range(budget, info['cost'] - 1, -1):
            if dp[cost - info['cost']] + info['calories'] > dp[cost]:
                dp[cost] = dp[cost - info['cost']] + info['calories']
                selected_items[cost] = selected_items[cost - info['cost']] + [item]

    return selected_items[budget], dp[budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print(dynamic_programming(items, budget))
