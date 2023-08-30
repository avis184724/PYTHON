import random

def Card_Select():
    dd =1
while(1):
    
    # 게임을 할 것인지 묻기
    Game_Start = input("게임을 시작하려면 y 아니라면 n을 눌러주세요 : ")
    if(Game_Start == "n"):
        break

    # 2차원 배열로 카드 입력
    card = [
            ["Spade Ace", "Spade 2", "Spade 3", "Spade 4", "Spade 5", "Spade 6", "Spade 7", "Spade 8", "Spade 9", "Spade 10", "Spade Jack", "Spade Queen", "Spade King"],
            ["Diamond Ace", "Diamond 2", "Diamond 3", "Diamond 4", "Diamond 5", "Diamond 6", "Diamond 7", "Diamond 8", "Diamond 9", "Diamond 10", "Diamond Jack", "Diamond Queen", "Diamond King"],
            ["Heart Ace", "Heart 2", "Heart 3", "Heart 4", "Heart 5", "Heart 6", "Heart 7", "Heart 8", "Heart 9", "Heart 10", "Heart Jack", "Heart Queen", "Heart King"],
            ["Clover Ace", "Clover 2", "Clover 3", "Clover 4", "Clover 5", "Clover 6", "Clover 7", "Clover 8", "Clover 9", "Clover 10", "Clover Jack", "Clover Queen", "Clover King"],
            ]

    # 1번 플레이어의 1번 카드   
    First_Player_First_x = random.randrange(0,4)
    First_Player_First_y = random.randrange(0,13)
    First_Player_First_Card = card[First_Player_First_x][First_Player_First_y]
    print(First_Player_First_Card)

    # 1번 플레이어의 2번 카드
    First_Player_Second_x = random.randrange(0,4)
    First_Player_Second_y = random.randrange(0,13)
    First_Player_Second_Card = card[First_Player_Second_x][First_Player_Second_y]
    print(First_Player_Second_Card)