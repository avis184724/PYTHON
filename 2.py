
def stair() :
    a = int(input("칸 수 : "))
    print()

    for i in range(a):
        print("  "*i +"* "*(a-i))
        i = i + 1


def spuare() :
    while(1):
        b = int(input("칸 수 (5 이상의 홀수만) : "))
        if b >= 5 and b % 2 == 1 :
            break
        else :
            continue

    for i in range(1,b+1):
        print("  "*(b-i)+"* "*(i*2-1))
    for j in range(b-1, 0, -1):
        print("  "*(b-j)+"* "*(j*2-1))

while(1):
    choose = int(input("어떤 삼각형을 출력하겠습니까? (마름모 : 1 직각삼각형 : 2) : "))
    if choose == 1:
        print()
        spuare()
        print()
    elif choose == 2:
        print()
        stair()
        print()
    else :
        print("\n다시 선택하세요\n")
        continue
