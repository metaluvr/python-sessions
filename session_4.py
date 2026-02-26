def session_4():

    a = int(input("1부터 n까지의 합:"))
    total_sum = 0
    for i in range(1, a + 1):
        total_sum = total_sum + i

    print(f"1부터 {a}까지의 합: {total_sum}")
    
    b = int(input("n의 배수:"))
    c = int(input("n의 배수로 몇까지 더할지:"))
    multiple_sum = 0
    for j in range(b, c + 1):
        if j % b == 0:
            multiple_sum = multiple_sum + j

    print(f"{b}의 배수 만으로 {c}까지의 합: {multiple_sum}")
    
session_4()