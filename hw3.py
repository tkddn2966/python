def get_fixed_price(n):
    global discount
    return n / (1-(discount/100 ))

discount = int(input("할인률은 ? :"))
a = int(input("A 상품의 할인된 가격은? :"))
b = int(input("B 상품의 할인된 가격은? :"))
print("A 상품의 정가는 ",get_fixed_price(a),"원")
print("B 상품의 정가는 ",get_fixed_price(b),"원")
