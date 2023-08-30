height = float(input("키를 입력하세요 : ")) # 키 입력 받기
weight = float(input("몸무게를 입력하세요 : ")) # 몸무게 입력 받기

BMI = float(weight / (height/100) ** 2 ) # 입력 받은 키와 몸무게를 계산해서 BMI에 넣기

print("BMI 지수는 ", round(BMI, 2) , " 입니다.") # BMI를 소수점 2번째 자리까지 반올림 후 출력