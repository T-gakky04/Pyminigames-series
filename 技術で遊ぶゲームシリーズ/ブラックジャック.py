import random

RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['♠', '♣', '♡', '♢']

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10,
    'A': 11
}

#カード
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def get_value(self):
        return CARD_VALUES[self.rank]

    def __str__(self):
        return f'{self.suit}{self.rank}'
    
    def __repr__(self):
        return self.__str__()

#デッキ
class Deck:
    def __init__(self):
        self.cards = []

        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(suit,rank))
        
        random.shuffle(self.cards)
    
    def __str__(self):
        return f'{self.cards[0].get_value()}'
    
    def draw(self):
        draw_card = self.cards.pop(0)
        return draw_card

#点数計算。22点以上のときはAの点数調整
def calculate_score(user_hands):
    score = 0
    ace_count = 0
    for card in user_hands:
        score += card.get_value()
        if card.get_value() == 11:
            ace_count += 1

    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score

#プレイヤーの手札とスコア表示
def show_score(player_type, hands):
    print(f"{player_type}の手札：{hands}")
    print(f"{player_type}のスコア：{calculate_score(hands)}")

deck = Deck()

#2枚ずつ引く
player_hands = [deck.draw() for _ in range(2)]
cpu_hands = [deck.draw() for _ in range(2)]

#CPUは手札が14以下の時に機械的に引く。
while calculate_score(cpu_hands) < 15:
    cpu_hands.append(deck.draw())

show_score("プレイヤー", player_hands)

while True:
    draw_flag = input("もう1枚カードを引きますか？（y/n）：").lower()
    if draw_flag == "y":
        player_hands.append(deck.draw())
    elif draw_flag == "n":
        show_score("プレイヤー", player_hands)
        break
    else:
        print("yかnで回答してください。")
    
    show_score("プレイヤー", player_hands)

    #バースト処理
    if calculate_score(player_hands) > 21:
        print("21を超えました。バーストです。")
        break
    
#勝敗処理 プレイヤーのバーストと同点はプレイヤーの負け
if calculate_score(player_hands) > 21:
    print("プレイヤーの負けです。")
elif calculate_score(cpu_hands) > 21:
    show_score("CPU", cpu_hands)
    print("CPUはバーストしました。")
    print("プレイヤーの勝ちです。")
elif calculate_score(player_hands) > calculate_score(cpu_hands):
    show_score("CPU", cpu_hands)
    print("プレイヤーの勝ちです。")
else:
    show_score("CPU", cpu_hands)
    print("プレイヤーの負けです。")