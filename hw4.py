def draw_line_string(n):
    msg2 = "Welcome to seoul."
    nstr = len(n) if (len(n) > len(msg2)) else len(msg2)
    print("-"*nstr)
    print("Hello",n+",\n"+msg2)
    print("-"*nstr)

draw_line_string(input("input his/her name : "))
