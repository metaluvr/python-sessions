def session_3():
    num = int(input("숫자 입력:"))

    if num > 0:
        print("양수")
    
    elif num < 0:
        print("음수")

    else:
        print("0입니다")

    if num % 2 == 0:
        print("짝수")
    else:
        print("홀수")
        
session_3()