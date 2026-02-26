def session_6():
    
    a = int(input("검사 항목수:"))
    for i in range(a):
        b = input("검사할 대상:")
        c = int(input(f"{b}의 검사 시행 횟수:"))
        d = int(input(f"{b}의 검사 합격 기준:"))
        p = [] # 합격
        f = [] # 불합격
        print(f"{b}의 검사를 시작합니다")
        for j in range(c):
            e = int(input(f"{b}의 중량:"))
            if e >= d:
                p.append(e)
                print(f"합격 {b}입니다")
            else:
                f.append(e)
                print(f"불합격 {b}입니다")

        print(f"-----{b}의 검사결과-----")        
        
        def result(data, label):
            print(f"[{label}]")
            print(f"{b}의 총 {label} 수량은 {len(data)}개 입니다")
            print(f"{b}의 최소 중량은 {min(data)}kg 입니다")
            print(f"{b}의 최대 중량은 {max(data)}kg 입니다")
            print(f"{b}의 평균 중량은 {sum(data)/len(data):.2f}kg 입니다")

        if len(p) > 0:
            result(p, "합격")
        else:
            print(f"{b}의 합격 데이터가 없습니다")

        if len(f) > 0:
            result(f, "불합격")
        else:
            print(f"{b}의 불합격 데이터가 없습니다")
        
session_6()