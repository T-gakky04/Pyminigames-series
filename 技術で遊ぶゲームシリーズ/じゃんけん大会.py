import random

HANDS = ["グー", "チョキ", "パー"]
WIN_MAP = {
    "グー" : "チョキ",
    "チョキ" : "パー",
    "パー" : "グー"
}

#じゃんけんの手が選択される処理
def choose_hand():
    hand = random.choice(HANDS)
    return hand

#じゃんけんの勝敗判定処理
def judge_winner(hand1, hand2):
    if hand1 == hand2:
        result = "draw"
        winning_hand = None
    elif WIN_MAP[hand1] == hand2:
        result = "win"
        winning_hand = hand1
    else:
        result = "lose"
        winning_hand = hand2
    
    return result, winning_hand

win_count ={"グー" : 0, "チョキ" : 0, "パー" : 0}

players = []
winners = []

num_players = int(input('プレイヤーの人数を決定してください'))

for i in range(num_players):
    hand1 = choose_hand()
    hand2 = choose_hand()

    result, winning_hand = judge_winner(hand1, hand2)
    
    #勝った手を保存
    if winning_hand:
        win_count[winning_hand] += 1

print(win_count)