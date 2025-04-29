a = {}
print("[구입]")
while True:
    item = input("상품명? ")
    if item == "":
        break
    count = int(input("수량은? "))
    a[item] = count
    print(f"장바구니에 {item} {count}개 담겼습니다.\n")

print(f">>>장바구니 보기 : {a}\n")

b = input("장바구니에서 확인하고자 하는 상품은? ")
print(f"{b}은(는) {a[b]}개 담겨 있습니다.")
