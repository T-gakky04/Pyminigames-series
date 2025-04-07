import random

element_multiplier_map = {
    "fire": {
        "grass": 2.0,
        "water": 0.5,
    },
    "water": {
        "fire": 2.0,
        "water": 0.5,
    },
    "grass": {
        "water": 2.0,
        "fire": 0.5,
    },
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
        base_damage = max(0, (self.ATK / 2 - target.DEF / 4))
        damage = int(base_damage  *  random_multiplier)
        target.HP -= damage

    def __str__(self):
        return f'{self.name} (HP={self.HP}, ATK={self.ATK}, DEF={self.DEF}, SPD={self.SPD}, 属性={self.element})'

#先行判定
#player_initiative = random.gauss(player.SPD, player.SPD * 0.2)
    
pika = Character('ピカチュウ', 100, 150, 50, 100, 50)
hito = Character('ヒトカゲ', 100, 50, 50, 100, 50)

pika.attack(hito)

print(pika)
print(hito)