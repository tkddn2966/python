shopping_bag = {} #장바구니

def show(n):
    print(f">>>장바구니 보기 : {n}")

def find(n):
    print("[검색]")
    b = input("장바구니에서 확인하고자 하는 상품은? \n")
    if b in n:
        print(f"{b}은(는) {n[b]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {b}는 없습니다.")


def buy(n):
    print("[구입]")
    item = input("상품명? ")
    if item != "":
        count = int(input("수량은? "))
        shopping_bag[item] = count
        print(f"장바구니에 {item} {count}개 담겼습니다.\n")
    else:
        return False
   
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
