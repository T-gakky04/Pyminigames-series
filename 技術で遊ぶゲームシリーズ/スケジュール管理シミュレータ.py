from datetime import datetime, date

schedules = {}

#日付を正しい型で返す関数
def input_to_date():
    while True:
        user_input = input("日付を入力してください（例：2025-4-20）：")
        try:
            return datetime.strptime(user_input, "%Y-%m-%d").date()
        except ValueError:
            print("入力形式が正しくありません。再度入力してください。")

#日付表示を加工する関数
def format_date(date_obj):
    return date_obj.strftime("%Y年%#m月%#d日")

#スケジュール入力
def create_schedule(schedules):

    print("スケジュールに予定を入力します。")
    input_date = input_to_date()
    formatted = format_date(input_date)

    if input_date in schedules:
        print(f'{formatted}はすでに予定が登録されています。')
    else:
        schedules[input_date] = input("予定を入力してください：")
        print(f'{formatted}の予定が登録されました。')

#スケジュール確認
def read_schedule(schedules):

    print("スケジュールを確認します。")
    input_date = input_to_date()
    formatted = format_date(input_date)

    if input_date in schedules:
        print(f'{formatted}の予定は{schedules[input_date]}です。')
    else:
        print(f'{formatted}に予定は登録されていません。')

#スケジュール更新
def update_schedule(schedules):
    print("スケジュールを更新します。")
    input_date = input_to_date()
    formatted = format_date(input_date)

    if input_date in schedules:
        print(f'{formatted}の現在登録されている予定は{schedules[input_date]}です。')
        schedules[input_date] = input("新しい予定を入力してください：")
        print(f'{formatted}の予定が更新されました。')
    else:
        print(f'{formatted}に予定は登録されていません。')

#スケジュール削除
def delete_schedule(schedules):
    print("スケジュールを削除します。")
    input_date = input_to_date()
    formatted = format_date(input_date)

    if input_date in schedules:
        print(f'{formatted}の現在登録されている予定は{schedules[input_date]}です。')
        removed_value = schedules.pop(input_date)
        print(f'{formatted}の予定（{removed_value}）削除しました。')
    else:
        print(f'{formatted}に予定は登録されていません。')

#スケジュール一覧表示（日付順に並び替え）
def show_schedule(schedules):
    print("--- 登録された予定 ---")
    for date_obj in sorted(schedules):
        print(format_date(date_obj), schedules[date_obj])
    print("---------------------")

def run_schedule_app(schedules):
    while True:
        print("1:追加 2:確認 3:更新 4:削除 5:一覧表示 6:終了")

        try:
            menu_choice = int(input("番号を入力してください（1〜6）:"))
        except ValueError:
            print("無効な入力です。1～6の数値を入力してください。")
            continue

        action = menu_actions.get(menu_choice)

        if menu_choice == 6:
            print("終了します。")
            break
        elif menu_choice in menu_actions:
            action(schedules)
        else:
            print("無効な入力です。1～6の数値を入力してください。")

menu_actions = {
    1: create_schedule,
    2: read_schedule,
    3: update_schedule,
    4: delete_schedule,
    5: show_schedule
}

run_schedule_app(schedules)