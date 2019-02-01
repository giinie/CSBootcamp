# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: n개의 이름 중 반복되는 이름의 집합

def find_same_name(a):
    # 1단계: 각 이름의 등장 횟수를 딕셔너리로 만듦
    name_dict = {}
    for name in a:  # 리스트 a에 있는 자료들을 차례로 반복
        if name in name_dict:     # 이름이 name_dict에 있으면
            name_dict[name] += 1  # 등장 횟수를 1 증가
        else:                     # 새 이름이면
            name_dict[name] = 1   # 등장 횟수를 1로 저장

    # 2단계: 만들어진 딕셔너리에서 등장 횟수가 2 이상인 것을 결과에 추가
    result = set()  # 결괏값을 저장할 빈 집합
    for name in name_dict:  # 딕셔너리 name_dict에 있는 자료들을 차례로 반복
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["Tom", "Jerry", "Mike", "Tom"]  # 대소문자 유의: 파이썬은 대소문자를 구분함
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))
