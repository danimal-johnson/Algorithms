#!/usr/bin/python

import argparse


def find_max_profit(prices):
    num_prices = len(prices)
    if num_prices < 2:
        return 0

    max_profit = prices[1] - prices[0]

    # Buy at any index except the last one.
    for buy_index in range(num_prices-1):
        # Sell at any index after the purchased one.
        for sell_index in range(buy_index + 1, num_prices):
            # print("{} vs [{}]-[{}]".format(max_profit, sell_index, buy_index))
            max_profit = max(max_profit, prices[sell_index]-prices[buy_index])

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
