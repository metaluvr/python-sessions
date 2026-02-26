def session_2():
    a = input("첫번째 숫자:")
    b = input("두번째 숫자:")

    result_1 = int(a) + int(b)
    result_2 = int(a) - int(b)
    result_3 = int(a) * int(b)
    result_4 = int(a) / int(b)

    print(f"합: {result_1}")
    print(f"차: {result_2}")
    print(f"곱: {result_3}")
    print(f"나눗셈: {result_4}")
    
session_2()