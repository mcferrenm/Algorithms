#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_price_so_far = float("inf")
    max_profit = 0
    for p in prices:
        print(max_profit, p - min_price_so_far)
        max_profit = max(max_profit, p - min_price_so_far)
        min_price_so_far = min(p, min_price_so_far)
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
