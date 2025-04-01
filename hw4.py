def draw_line_string(n):
    msg1 = " hello " +n
    msg2 = "Welcome to seoul."
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char("-",nstr)
    print("Hello",n+",\n"+msg2)
    rep_char("-",nstr)

def rep_char(s,d):
    print(s*d)

draw_line_string(input("input his/her name : "))

