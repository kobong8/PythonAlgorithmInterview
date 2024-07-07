def bf_match(txt: str, pat: str) -> int:
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


if __name__ == "__main__":
    print("main")


# Reference
# Do it! 자료구조와 함께 배우는 알고리즘 입문: 파이썬 편