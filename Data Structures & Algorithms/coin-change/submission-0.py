class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins_seen = {0: 0}

        def dfs(target: int) -> int:
            if target in min_coins_seen:
                return min_coins_seen[target]
            if target < 0:
                return float('inf')

            min_coins = float('inf')
            for coin_value in coins:
                min_children_coins = dfs(target - coin_value)
                min_coins = min(min_coins, min_children_coins + 1)
            
            min_coins_seen[target] = min_coins
            return min_coins

        result = dfs(amount)
        return result if result != float('inf') else -1