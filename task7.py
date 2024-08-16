import random

import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(trials):
    results = [0] * 11

    for _ in range(trials):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        results[dice_sum - 2] += 1

    probabilities = [result / trials for result in results]

    return probabilities


probabilities = monte_carlo_dice_simulation(10000)

plt.bar(range(2, 13), probabilities)
plt.xlabel('Sum')
plt.ylabel('Probability')
plt.title('Probabilities for Dice Sums (Monte Carlo Method)')
plt.show()
