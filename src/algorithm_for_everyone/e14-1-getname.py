# 학생 번호에 해당하는 학생 이름 찾기(dict 이용)
# 입력: 학생 명부 딕셔너리 s_info, 찾는 학생 번호 find_no
# 출력: 해당하는 학생 이름, 해당하는 학생 번호가 없으면 물음표 "?"

def get_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else:
        return "?"  # 해당하는 번호가 없으면 물음표 

sample_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(get_name(sample_info, 105))
print(get_name(sample_info, 777))
