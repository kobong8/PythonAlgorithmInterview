# %%
# [1] brute force method
def bf_match(txt: str, pat: str) -> int:
    print("Brute Force Method")
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp +1
            pp = 0

    return pt - pp if pp == len(pat) else -1

# %%
# [2] Knuth-Morris-Pratt(KMP) method 
# TODO while 문이 2개가 돌아가니깐 연산 시간 확인 필요
# TODO 문자열이 증가하니깐 연산 결과도출이 안됨
def kmp_match(txt: str, pat: str) -> int:
    print("Knuth-Morris-Pratt(KMP) Method")
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    # KMP Table
    # TODO 위에서 0으로 다 채웠는데 필요한건지?
    # skip[pt] = 0 
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp 
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp == skip[pp]
    print(skip)
    
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    print(skip)

    return pt - pp if pp == len(pat) else -1

# %%
# [3] Boyer-Moor Method
def bm_match(txt: str, pat: str) -> int:
    print("Boyer-Moor Method")
    skip = [None] * 256

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1
    # print(skip)

    # 검색하기

    return -1

# %%
if __name__ == "__main__":
    s1 = "ADJNSABAISABCAJSDQNRMZPD"
    s2 = "ABCA"
    # s2 = "ABCAJ"

    # [1] Test brute force method
    idx = bf_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"{idx+1}번째 문자가 일치합니다.")

    # [2] Test brute force method
    idx = kmp_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"{idx+1}번째 문자가 일치합니다.")

    # [3] Boyer-Moor Method
    idx = bm_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"{idx+1}번째 문자가 일치합니다.")

# Reference
# Do it! 자료구조와 함께 배우는 알고리즘 입문: 파이썬 편


