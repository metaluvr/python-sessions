def session_1():
    a = 7

    if a > 5:
        print("크다")
    else:
        print("작다")

    for i in range(1,6):
        print(i)

    arr = [3, 7, 2, 9]

    for x in arr:
        if x > 5:
            print(x)

    name = input("이름 입력:")
    age = input("나이 입력:")

    print("안녕하세요", name)
    print(f"당신의 나이는 {age}세 입니다")
    
session_1()