height = float(input("키를 입력하세요 : ")) # 키 입력 받기
weight = float(input("몸무게를 입력하세요 : ")) # 몸무게 입력 받기

BMI = round(float(weight / (height/100) ** 2 ),2) # 입력 받은 키와 몸무게를 계산해서 BMI에 넣기

# 저체중,정상,과체중 계산 ( 범위 : 10대 후반 )
if(BMI < 18):
    print("BMI 지수는 ", BMI, "로 저체중 입니다.") # BMI를 소수점 2번째 자리까지 반올림 후 출력
elif(BMI < 25):
    print("BMI 지수는 ", BMI, "로 정상 입니다.") # BMI를 소수점 2번째 자리까지 반올림 후 출력
else:
    print("BMI 지수는 ", BMI, "로 과체중 입니다.") # BMI를 소수점 2번째 자리까지 반올림 후 출력