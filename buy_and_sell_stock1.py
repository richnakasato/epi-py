from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    if not prices or len(prices) < 2:
        return 0
    else:
        min_so_far = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_so_far)
            min_so_far = min(min_so_far, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
