# 학생 번호에 해당하는 학생 이름 찾기
# 입력: 학생 번호 리스트 s_no, 학생 이름 리스트 s_name, 찾는 학생 번호 find_no
# 출력: 해당하는 학생 이름, 학생 이름이 없으면 물음표 "?"

def get_name(s_no, s_name, find_no):
    n = len(s_no)  # 입력 크기 n
    for i in range(0, n):
        if find_no == s_no[i]: # 학생 번호가 찾는 학생 번호와 같으면
            return s_name[i]   # 해당하는 학생 이름을 결과로 반환

    return "?"  # 자료를 다 뒤져서 못 찾았으면 물음표 반환

sample_no = [39, 14, 67, 105]
sample_name = ["Justin", "John", "Mike", "Summer"]
print(get_name(sample_no, sample_name, 105))
print(get_name(sample_no, sample_name, 777))
