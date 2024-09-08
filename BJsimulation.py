import random
from collections import deque
import numpy as np


# 建立一副牌
def create_deck():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"] * 4
    random.shuffle(deck)
    return deque(deck)


# 計算手牌點數
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card in "TJQK":
            value += 10
        elif card == "A":
            num_aces += 1
            value += 11
        else:
            value += int(card)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value


# 發牌
def deal_card(deck):
    return deck.popleft()


# 根據算牌策略決定玩家是否應該獲勝
def should_player_win(deck, seen_cards):
    count = 0
    for card in seen_cards:
        if card in "23456":
            count += 1
        elif card in "TJQKA":
            count -= 1

    # 正數意味著大牌剩餘較多，負數意味著小牌剩餘較多
    return count > 0


# 模擬一局遊戲
def simulate_single_game(deck, seen_cards):
    dealer_hand = [deal_card(deck), deal_card(deck)]
    player_hand = [deal_card(deck), deal_card(deck)]

    seen_cards.extend(dealer_hand + player_hand)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value == 21 and dealer_value != 21:
        return True  # Player wins with Black Jack
    elif dealer_value == 21:
        return False  # Dealer wins with Black Jack

    return should_player_win(deck, seen_cards)


# 模擬多局遊戲
def simulate_multiple_games(num_games=100000):
    wins = 0
    deck = create_deck()
    seen_cards = []

    for _ in range(num_games):
        if len(deck) < 10:
            deck = create_deck()
            seen_cards = []
        if simulate_single_game(deck, seen_cards):
            wins += 1

    return wins / num_games


# 計算並顯示玩家的獲勝機率
def display_win_probability():
    num_games = 100000
    win_probability = simulate_multiple_games(num_games)
    print(f"Player's win probability: {win_probability:.4f}")


if __name__ == "__main__":
    display_win_probability()
