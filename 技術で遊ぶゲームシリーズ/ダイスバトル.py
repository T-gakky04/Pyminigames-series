import random

#サイコロを振る処理
def roll_dice(player_type):
    dice = random.randint(1, 6)
    print(f'{player_type}:{dice}が出ました')
    return dice

#勝敗を判定する処理
def judge_winner(player_rolls, cpu_rolls):
    #出目を合算
    player_total = sum(player_rolls)
    cpu_total = sum(cpu_rolls)

    #合計値を出力
    print(f"プレイヤー合計：{player_total}、CPU合計：{cpu_total}")

    if player_total > cpu_total:
        print("プレイヤーの勝ちです！")
    
    elif cpu_total > player_total:
        print("CPUの勝ちです。")
    
    else:
        print("引き分けです。")

#サイコロ個数を手入力を決める処理
def input_dice_count(player_type):
    while True:
        dice_count = input(f'{player_type}のサイコロ個数を入力してください。')
        if dice_count.isdigit():
            dice_count = int(dice_count)
            print(f'{player_type}のサイコロ個数は{dice_count}個です。')
            return dice_count
        else:
            print("⚠️ 数字で入力してください。")

#サイコロ個数を自動で決める処理
def random_dice_count(player_type):
    #とりあえず最大5個
    dice_count = random.randint(1, 5)
    print(f'{player_type}のサイコロ個数は{dice_count}個です。')
    return dice_count

#決められた回数サイコロを振り、リストとして返す
def roll_dice_list(count, player_type):
    #空のリスト作成
    rolls = []
    for i in range(count):
        rolls.append(roll_dice(player_type))
    return rolls

#メイン処理
def main():
    
    while True:
        mode = input('サイコロ個数を決める方法を選んでください（manual / auto）：').lower()
        if mode == 'manual':
            #手動
            player_dice_count = input_dice_count("プレイヤー")
            cpu_dice_count = input_dice_count("CPU")
            break

        elif mode =='auto':
            #自動
            player_dice_count = random_dice_count("プレイヤー")
            cpu_dice_count = random_dice_count("CPU")
            break

        else:
            print("manualかautoを入力してください。")

    #プレイヤーごとにサイコロの出目リストを作成
    player_rolls = roll_dice_list(player_dice_count, "プレイヤー")
    cpu_rolls = roll_dice_list(cpu_dice_count, "CPU")

    #勝敗判定
    judge_winner(player_rolls, cpu_rolls)

if __name__ == "__main__":
    main()
