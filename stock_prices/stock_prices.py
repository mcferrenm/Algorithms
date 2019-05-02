#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_price_so_far = float("inf")
    current_max_profit = float("-inf")
    max_profit = float("-inf")
    for p in prices:
        current_max_profit = p - min_price_so_far
        
        if p < min_price_so_far:
            min_price_so_far = p
        
        if current_max_profit > max_profit:
            max_profit = current_max_profit

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
