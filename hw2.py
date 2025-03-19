
def get_integer(p):
    n = int(input(p))
    return n

def exchange(m):
    f = m // 500
    fa = m % 500
    o = fa // 100
    oa = fa % 100
    fi = oa // 50
    fia = oa % 50
    one = fia // 10
    print("500원 동전의 개수 :",f)
    print("100원 동전의 개수 :",o)
    print("50원 동전의 개수 :",fi)
    print("10원 동전의 개수 :",one)


result = get_integer("동전으로 교환하고자 하는 금액은 ? :")
exchange(result)
