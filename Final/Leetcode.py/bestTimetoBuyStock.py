from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices: # Check if the list is empty
        return 0
    
    min_price = float('inf')  # set the min_price to infinity, so that any price will be updated
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit

def main():
    price_list = list(map(int, input().split()))
    print(price_list)
    print(maxProfit(price_list))

if __name__ == "__main__":
    main()
