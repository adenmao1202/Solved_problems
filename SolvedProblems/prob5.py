import json


def MA_10(closing_prices):
    if len(closing_prices) < 10:  # 如果長度小於10，就無法計算。大於時，可以計算
        return None
    else:
        return int(sum(closing_prices[-10:]) / 10)  # -10 ~ -1(也就是最新的價格)


def select_stocks(input):
    try:
        stocks = json.loads(input)
    except json.decoder.JSONDecodeError:
        return None

    selected_num = 0
    for (
        ticker,
        prices,
    ) in stocks.items():  # dictionary call: for key, value in dictionary.items()
        # dictionary.keys()
        # dictionary.values()
        ma10 = MA_10(prices)  # call func
        if ma10 is not None and prices[-1] > ma10:  # -1 是最新的價格 > 10日平均價格
            selected_num += 1

    return selected_num


if __name__ == "__main__":
    direct_in = input()
    result = select_stocks(direct_in)  # call func
    if result is not None:
        print(result)
