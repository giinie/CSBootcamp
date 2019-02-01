# 주어진 문장이 회문인지 확인(문자열의 앞뒤를 서로 비교)
# 입력: 문자열 s 
# 출력: 회문이면 True, 아니면 False

def palindrome(s):
    i = 0          # 문자열의 앞에서 비교할 위치
    j = len(s) - 1 # 문자열의 뒤에서 비교할 위치
    while i < j:   # 중간까지만 검사하면 됨
        # i 위치에 있는 문자가 알파벳 문자가 아니면 뒤로 이동
        if s[i].isalpha() == False:
            i += 1
        # j 위치에 있는 문자가 알파벳 문자가 아니면 앞으로 이동
        elif s[j].isalpha() == False:
            j -= 1
        # i, j 위치 둘다 알파벳 문자가 있으면 두 문자를 비교하고 다르면 회문이 아님
        elif s[i].lower() != s[j].lower():
            return False
        # i와 j 위치에 두 문자를 비교하고 같으면 다음 비교 대상으로 넘어감
        else:
            i += 1
            j -= 1

    return True

print(palindrome("Wow"))
print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))
