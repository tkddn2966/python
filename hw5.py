def read_single_digit(n):
    a = int(n[0])
    return a

def read_number(a):
    if a == 1:
        return "일"
    elif a == 2:
        return "이"
    elif a == 3:
        return "삼"
    elif a == 4:
        return "사"
    elif a == 5:
        return "오"
    elif a == 6:
        return "육"
    elif a == 7:
        return "칠"
    elif a == 8:
        return "팔"
    elif a == 9:
        return "구"
    elif a == 0:
        return "영"
    
    

num = input("세 자리 정수 입력 :")
res = read_single_digit(num[0])
print(read_number(res), end =" ")
res = read_single_digit(num[1])
print(read_number(res), end =" ")
res = read_single_digit(num[2])
print(read_number(res), end =" ")
