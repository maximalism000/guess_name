print('名前を入力してください')
true_name = list(input())

print('試行回数を入力してください')
N = int(input())


game_continue = True
LEN_NAME = '=====名前は%d文字です=====' % len(true_name)
user_change = '''






======================回答者に渡してください=========================






'''

print(user_change)

rule = '''名前当てゲームのルールを説明します。
最初に、出題者が名前と試行回数を決めます。
次に、回答者は、名前の文字数と試行回数を知ることできます。
回答者が名前を入力すると、それに対して更に多くの情報が得られます。
hit: 文字が名前に含まれており、尚且つ、位置が正しい
ball: 文字が名前に含まれているが、位置が正しくない
strike: 文字が名前に含まていない
ではゲームを始めます\n\n'''

print(rule)
print(LEN_NAME)
print('=====試行回数は%d回です=====' % N)

while game_continue:
    for i in range(N):
        guess_name = list(input())
        hit = 0
        ball = 0
        strike = 0

        if len(guess_name) == len(true_name):
            for j in range(len(true_name)):

                if guess_name[j] == true_name[j]:
                    hit += 1
                elif guess_name[j] in true_name:
                    ball += 1
                else:
                    strike += 1
        else:
            print(LEN_NAME)

        print('hit: %d\nball: %d\nstrike: %d\n' % (hit, ball, strike))
        if hit == len(true_name):
            print('正解！')
            game_continue = False
            break

        else:
            print('=====試行回数は残り%d回です=====\n名前を予測してください' % (N - i - 1))
            if (N - i - 1) == 0:
                print('GAME OVER')
                game_continue = False
                break
