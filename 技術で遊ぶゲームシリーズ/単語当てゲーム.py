import random

def get_valid_guess(guessed_letters):
    #ユーザーに文字を入力してもらう
    guess = ''
    while True:
        guess = input('英単語を1文字入力してください').lower()
        if len(guess) != 1 or not guess.isalpha(): 
            print('半角英字1文字で入力してください。')
        elif guess in guessed_letters:
            print('その文字はすでに使われています。別の文字を入力してください')
        else:
            return guess

def print_word_state(display_word):
    print('現在の単語の状態：', ' '.join(display_word))

#関数作成中
def check_guess_and_update_display(guess, target_word, display_word):
    #単語の正誤判定
    for i in range(len(target_word)):
        #単語があっている場合は、単語を埋める
        if guess == target_word[i]:
            display_word[i] = guess
        else:
            pass
        
    #正誤表示。同じ文字が複数入っていることがあるので、最後にまとめて表示
    if guess in target_word:
        print(f'⭕️「{guess}」は正解です！残りライフ数は{miss_count}です。')
    else:
        miss_count -= 1
        print(f'❌「{guess}」はこの単語に含まれていません。残りライフ数は{miss_count}です。')

    if miss_count == 0:
        print('ライフ数が0になりました。ゲームを終了します。')
        print(f'正解の言葉は{target_word}でした。')
        

WORDS = {
    'easy': ['cat', 'dog', 'sun', 'car', 'hat'],
    'normal': ['planet', 'jungle', 'bridge', 'rocket'],
    'hard': ['astronomy', 'microscope', 'imagination']
}
DIFFICULTY_LEVELS = ['easy', 'normal', 'hard']

#ライフ数を入力する。
while True:
    miss_count = input('ライフ数を入力してください。')
    if miss_count.isdigit():
        miss_count = int(miss_count)
        break
    else:
        print("⚠️ 数字で入力してください。")

#ユーザーに難易度を選ばせる。選ぶまで無限ループ
selected_difficulty = None
while True:
    selected_difficulty = input('難易度を「easy」「normal」「hard」から選んでください。').lower()
    if selected_difficulty in DIFFICULTY_LEVELS:
        print(f'難易度{selected_difficulty}、ライフ数{miss_count}でゲームスタート！')
        break

#選択された難易度から単語を選ぶ
target_word = random.choice(WORDS[selected_difficulty])

#単語を表示する
display_word = ['_' for _ in target_word]
print_word_state(display_word)

guessed_letters = set()

#単語を当てる処理
while '_' in display_word:
    #ユーザーが文字を1文字入力する処理
    guess = get_valid_guess(guessed_letters)
    guessed_letters.add(guess)
    
    #単語の正誤判定
    for i in range(len(target_word)):
        #単語があっている場合は、単語を埋める
        if guess == target_word[i]:
            display_word[i] = guess
        else:
            pass
        
    #正誤表示。同じ文字が複数入っていることがあるので、最後にまとめて表示
    if guess in target_word:
        print(f'⭕️「{guess}」は正解です！残りライフ数は{miss_count}です。')
    else:
        miss_count -= 1
        print(f'❌「{guess}」はこの単語に含まれていません。残りライフ数は{miss_count}です。')

    if miss_count == 0:
        print('ライフ数が0になりました。ゲームを終了します。')
        print(f'正解の言葉は{target_word}でした。')
        break
    
    print_word_state(display_word)

#ライフ数が0になる前に正解したときの処理
if not '_' in display_word:
    print(f'あなたの勝ちです！正解の言葉は{target_word}でした。')