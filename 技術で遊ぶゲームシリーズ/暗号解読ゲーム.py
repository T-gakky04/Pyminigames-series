import string

#3文字ずらしの暗号
plain = list(string.ascii_lowercase)
cipher = plain[3:] + plain[:3]

#正しい言葉と暗号を辞書で結びつける
cipher_map = dict(zip(cipher, plain))

encrypted = 'khoor'

print(f"暗号文：{encrypted}")
guess = input("この暗号の正しい単語は？（英文小文字）").lower()

decrypted = ''.join(list(map(lambda ch:cipher_map.get(ch), encrypted)))

if guess == decrypted:
    print("正解！🎉")
else:
    print(f"残念！正解は：{decrypted}")