class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, len(min_coins)):
            min_cost = min_coins[i]
            for coin in coins:
                if i - coin >= 0: 
                    previous_coin = min_coins[i - coin] + 1
                    min_cost = min(min_cost, previous_coin)
            min_coins[i] = min_cost

        return min_coins[-1] if min_coins[-1] != float('inf') else -1