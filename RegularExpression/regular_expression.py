import re


if __name__ == "__main__":
    # 01 match
    p = re.compile("[a-z]+")
    m = p.match("python")
    print(m)

# Reference
# Do it! 점프 투 파이썬