import random

ELEMENT_MULTIPLIER_MAP = {
    "fire": {"grass": 1.2,"water": 0.8,},
    "water": {"fire": 1.2,"water": 0.8,},
    "grass": {"water": 1.2,"fire": 0.8,},
}

class Character:
    def __init__(self, name, HP, ATK, DEF, SPD, element):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SPD = SPD
        self.element = element
    
    def attack(self, target):
        random_multiplier = random.randint(85, 115)/100
        element_multiplier = ELEMENT_MULTIPLIER_MAP.get(self.element, {}).get(target.element, 1.0)
        base_damage = max(0, (self.ATK / 2 - target.DEF / 4))
        damage = int(base_damage  *  random_multiplier * element_multiplier)
        print(f'{self.name}の攻撃！{target.name}に{damage}のダメージ！')
        target.HP = max(0, target.HP - damage)

    def __str__(self):
        return f'{self.name} (HP={self.HP}, ATK={self.ATK}, DEF={self.DEF}, SPD={self.SPD}, 属性={self.element})'

#ターン中の処理
def turn_order(player, enemy):
    #乱数でターン中の優先度決定
    player_initiative = random.gauss(player.SPD, player.SPD * 0.35)
    enemy_initiative = random.gauss(enemy.SPD, enemy.SPD * 0.35)

    #同速の時はプレイヤー優先
    if player_initiative >= enemy_initiative:
        print(f'{player.name}が先制！')
        player.attack(enemy)
        
        #敵HPが0でないときは敵の攻撃
        if enemy.HP > 0:
            enemy.attack(player)
        
    else:
        print(f'{enemy.name}が先制！')
        enemy.attack(player)

        #自分のHPが0でないときは自分の攻撃
        if player.HP > 0:
            player.attack(enemy)

def main():
    player = Character('ゼニガメ', 114, 43, 77, 57, 'water')
    enemy = Character('ヒトカゲ', 109, 62, 55, 72, 'fire')

    #ターン数のカウント変数
    turn_count = 1

    while player.HP > 0 and enemy.HP > 0:
        print(f'{turn_count}ターン目')

        turn_order(player, enemy)

        print(player)
        print(enemy)

        turn_count += 1

if __name__ == "__main__":
    main()
