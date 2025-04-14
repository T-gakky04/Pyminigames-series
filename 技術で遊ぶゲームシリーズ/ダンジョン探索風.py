import random

MOVE_DICT = {
    "w" : (0, -1),
    "a" : (-1, 0),
    "s" : (0, 1),
    "d" : (1, 0)
}

MOVE_SET = {"w", "a", "s", "d"}

#マップ生成の関数
def generate_map(width, height):
    game_map = [["#" for x in range(width)] for y in range(height)]

    x, y = 1, 1
    goal_x, goal_y = width - 2, height - 2
    game_map[y][x] = "."

    while (x, y) != (goal_x, goal_y):
        direction = random.choice(["right", "down"])
        if direction == "right" and x < goal_x:
            x += 1
        elif direction == "down" and y < goal_y:
            y += 1
        # 失敗したらもう一度選び直す（何もせずループ）
        game_map[y][x] = "."

    #ランダムに通路を増やす
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if game_map[y][x] == "#":
                game_map[y][x] = "." if random.random() < 0.4 else "#"
    
    #スタート位置とゴール位置を明示する
    game_map[1][1] = "S"
    game_map[goal_y][goal_x] = "G"
    
    return game_map

#マップの表示
def print_map(game_map,player_pos = None):

    #表示用のマップ作成
    copied_map = [row.copy() for row in game_map]

    if player_pos:
        copied_map[player_pos[1]][player_pos[0]] = "P"
        
    for row in copied_map:
        print("".join(row))

#プレイヤーの移動関数
def move_player(game_map, player_pos):
    while True:
        move = input("移動(WASD)：").lower()
        if move in MOVE_SET:

            #移動先が壁でないときだけ移動する。壁の時は移動処理を停止する。
            if game_map[player_pos[1] + MOVE_DICT[move][1]][player_pos[0] + MOVE_DICT[move][0]] != "#":
                player_pos[0] += MOVE_DICT[move][0]
                player_pos[1] += MOVE_DICT[move][1]
            break
        else:
            print("WASDのいずれかを入力してください。")

#メイン処理
def main():
    #マップ生成
    game_map = generate_map(30, 10)

    #プレイヤーの初期位置
    player_pos = [1, 1]

    print_map(game_map)

    #ゴールに到達するまで
    while game_map[player_pos[1]][player_pos[0]] != "G":
        move_player(game_map,player_pos)
        print_map(game_map, player_pos)

    print("おめでとう！ゴールに到達しました！")

if __name__ == "__main__":
    main()