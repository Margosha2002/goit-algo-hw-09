def find_coins_greedy(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in denominations:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50][::-1]
    num_coins = [float("inf")] * (amount + 1)
    num_coins[0] = 0
    last_coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if num_coins[i - coin] + 1 < num_coins[i]:
                num_coins[i] = num_coins[i - coin] + 1
                last_coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


# Приклад використання:
amount = 113
greedy_result = find_coins_greedy(amount)
min_coins_result = find_min_coins(amount)

print("Greedy Algorithm Result:", greedy_result)
print("Dynamic Programming Result:", min_coins_result)
