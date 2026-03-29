# "낡은 수동 장치를 자동화 시스템으로"
# 과거의 코드가 "매번 물어보는 수동 측정기" 였다면, 오늘 만들 리마스터 버전은 "기준서를 알고 있는 스마트 판독기" 입니다.

# 활용할 재료들:
# 1. 중첩 딕셔너리 (Master Data): 재료별 S/A/B/C 기준과 완박스 수량을 미리 저장해둡니다. (매번 입력할 필요 X)
# 2. 판정 함수 (def & return): 품질과 수량을 계산해서 결과만 뱉어내는 독립 부품입니다.
# 3. 무한 루프 (while): 작업자가 "그만" 이라고 할 때까지 계속해서 검사를 수행합니다.
# 4. f-string: 결과를 아주 깔끔하게 출력합니다.


# Step 1: 기준서(Master Data) 만들기

# 재료별 기준 정보를 딕셔너리로 선언
material_standards = {
    "캡": {"S": 97, "A": 94, "B": 91, "C": 88, "target": 1000}, # 캡은 1000개가 완박스
    "펌프": {"S": 98, "A": 96, "B":94, "C": 92, "target": 350}, # 펌프는 350개가 완박스
    "용기": {"S": 99, "A": 98, "B": 97, "C": 96, "target": 168} # 용기는 168개가 완박스
}

# Step 2: 판정 기계(함수) 만들기

# 기계 1: 품질 판정기(judge_quality)

def judge_quality(score, std):
    """품질 점수와 해당 재료의 기준(std)을 받아 등급을 반환"""
    if score >= std["S"]:
        return "S급"
    elif score >= std["A"]:
        return "A급"
    elif score >= std["B"]:
        return "B급"
    elif score >= std["C"]:
        return "C급"
    else:
        return "불량"
    
# 기계 2: 수량 판정기(judge_quantity)

def judge_quantity(current_cnt, target_cnt):
    """실제 수량과 목표 수량을 받아 비율(%)과 상태를 반환"""
    # 계산식: (현재수량 / 목표수량) * 100
    ratio = (current_cnt / target_cnt) * 100

    if ratio >= 100:
        status = "완박스"
    elif ratio >= 95:
        status = "정상범위"
    else:
        status = "수량미달"

    return ratio, status # 파이썬은 이렇게 두 개의 결과물을 한 번에 뱉을 수도 있습니다!

# Step 3: 스마트 검사 루프

while True:
    mat_name = input("검사할 재료명(캡 / 펌프 / 용기)을 입력하세요 (종료하려면 'q'): ")

    if mat_name == 'q':
        break # 루프 탈출!

    if mat_name in material_standards:
        # 여기서 기준 정보를 쏙 뽑아옵니다.
        std = material_standards[mat_name]
        target_cnt = material_standards[mat_name]["target"]

        # 품질/수량 입력 받고 위에서 만든 함수에 '재료'로 던져줍니다.
        score = int(input(f"{mat_name}의 품질: "))
        quality_result = judge_quality(score, std)

        current_cnt = int(input(f"{mat_name}의 수량: "))
        quantity_result = judge_quantity(current_cnt, target_cnt)

        # 결과를 출력합니다.
        print(f"----- {mat_name}의 검사 결과 -----")
        print(f"{mat_name}의 품질은 {quality_result}입니다.")
        print(f"{mat_name}의 수량 비율(%)은 {quantity_result}입니다.")

    else:
        print("등록되지 않은 재료입니다. 다시 확인해 주세요.")