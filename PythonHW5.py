import json


def calculate_ma10(closing_prices):
    if len(closing_prices) < 10:
        return None
    else:
        return sum(closing_prices[-10:]) / 10


def select_stocks(json_input):
    data = json.loads(json_input)
    selected_stocks = 0

    for ticker, prices in data.items():
        ma10 = calculate_ma10(prices)
        if ma10 is not None and prices[-1] > ma10:
            selected_stocks += 1

    return selected_stocks


if __name__ == "__main__":
    json_input = input()
    result = select_stocks(json_input)
    print(result)
